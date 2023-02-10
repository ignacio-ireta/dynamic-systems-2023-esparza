from matplotlib import pyplot as plt
import numpy as np


def f(x, r):

    return x + r - x**2


fig, axs = plt.subplots(2, 3)
X0 = np.arange(0.1, 0.2, 0.1)

for x0 in X0:
    x = x0
    X = []
    r = 0.1
    for _ in range(0,30):
        X.append(x)
        x = f(x, r)
    axs[0, 0].plot(X)
    axs[0, 0].set_ylim(0, 2)
    axs[0, 0].set_xticks([*range(0,31,5)])
axs[0, 0].set_title(f'r = '+str(float(r)))

for x0 in X0:
    x = x0
    X = []
    r = 0.5
    for _ in range(0,30):
        X.append(x)
        x = f(x, r)
    axs[0, 1].plot(X)
    axs[0, 1].set_ylim(0, 2)
    axs[0, 1].set_xticks([*range(0, 31, 5)])
axs[0, 1].set_title(f'r = '+str(float(r)))

for x0 in X0:
    x = x0
    X = []
    r = 1.0
    for _ in range(0,30):
        X.append(x)
        x = f(x, r)
    axs[0, 2].plot(X)
    axs[0, 2].set_ylim(0, 2)
    axs[0, 2].set_xticks([*range(0, 31, 5)])
axs[0, 2].set_title(f'r = '+str(float(r)))

for x0 in X0:
    x = x0
    X = []
    r = 1.1
    for _ in range(0,30):
        X.append(x)
        x = f(x, r)
    axs[1, 0].plot(X)
    axs[1, 0].set_ylim(0, 2)
    axs[1, 0].set_xticks([*range(0, 31, 5)])
axs[1, 0].set_title(f'r = '+str(float(r)))

for x0 in X0:
    x = x0
    X = []
    r = 1.5
    for _ in range(0,30):
        X.append(x)
        x = f(x, r)
    axs[1, 1].plot(X)
    axs[1, 1].set_ylim(0, 2)
    axs[1, 1].set_xticks([*range(0, 31, 5)])
axs[1, 1].set_title(f'r = '+str(float(r)))

for x0 in X0:
    x = x0
    X = []
    r = 1.6
    for _ in range(0,30):
        X.append(x)
        x = f(x, r)
    axs[1, 2].plot(X)
    axs[1, 2].set_ylim(0, 2)
    axs[1, 2].set_xticks([*range(0, 31, 5)])
axs[1, 2].set_title(f'r = '+str(float(r)))

fig.tight_layout()
plt.show()