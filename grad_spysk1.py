import math
import numpy as np
from scipy.misc import derivative
from matplotlib import pyplot as plt


class GRADIUNT:
    def f(self, x):
        return (x - 5) ** 2

    def fp(self,x,eps):
        return (self.f(x+eps)-self.f(x))/eps

    def compute_gd(self, alpha=0.1, eps=0.00001, epoch=1000):
        x = []
        y = []
        data = {}
        x.append(0)
        y.append(self.f(x[0]))
        for i in range(1, epoch):
            #x.append(x[i - 1] - alpha * self.fp(x[i-1],eps))
            x.append(x[i - 1] - alpha * derivative(self.f, x[i - 1]))
            y.append(self.f(x[i]))
            data[x[i]] = y[i]
            if abs(x[i] - x[i - 1]) <= eps:
                return data
        return data

    def show_graph(self):
        t = np.linspace(0, 10, 20)
        yt = self.f(t)
        data_gd = self.compute_gd()
        x = data_gd.keys()
        y = data_gd.values()
        plt.plot(t, yt, 'g^',
                 x, y, 'ro--')
        plt.legend(['y = (x - 5)**2',
                    'GD method'])
        plt.annotate('min', xy=(5, 0), xytext=(5, 2),
                     arrowprops=dict(facecolor='yellow', shrink=1))
        plt.grid(True)
        plt.show()


if __name__ == '__main__':
    a = GRADIUNT()
    data = a.compute_gd()
    a.show_graph()
    print('data=', data)
