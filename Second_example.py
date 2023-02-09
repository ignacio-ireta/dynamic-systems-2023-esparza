from matplotlib import pyplot as plt
import numpy as np


# def f(x, a, b):
#
#     return a * x + b

def f(x, r):

    return x + r - x**2



def main():

    X0 = np.arange(0.1, 0.2, 0.1)

    for x0 in X0:
        # a = 0.5
        # b = 3.0
        # x0 = 0.5
        r = 10
        N = 100
        i = np.arange(0, N, 1)
        x = x0
        X = []

        for _ in i:
            X.append(x)
            x = f(x, r)

        plt.plot(X)
#    plt.yscale('log')
#    plt.ylim(0, 100)
    plt.show()


main()
