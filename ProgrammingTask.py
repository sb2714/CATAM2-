import numpy as np


def f(x, y):
    return -8 * y + 6 * np.exp(-2 * x)


def ye(x):
    return np.exp(-2 * x) - np.exp(-8 * x)


def forwardEuler(y0, x0, h, N):
    y = [y0]
    for n in range(1, N + 1):
        y.append(y[n - 1] + h * f(x0 + (n - 1) * h, y[n - 1]))
    print(y)
    return y


def AB2(y0, x0, h, N):
    y = forwardEuler(y0, x0, h, 1)
    for n in range(2, N + 1):
        y.append(y[n - 2] + h * (1.5 * f(x0 + h * (n - 1), y[n - 1]) - 0.5 * f(x0 + h * (n - 2), y[n - 2])))

    return y


def RK4(y0, x0, h, N):
    y = [y0]
    for n in range(1, N + 1):
        k1 = f(x0 + (n - 1) * h, y[n - 1])
        k2 = f(x0 + (n - 0.5) * h, y[n - 1] + 0.5 * h * k1)
        k3 = f(x0 + (n - 0.5) * h, y[n - 1] + 0.5 * h * k2)
        k4 = f(x0 + n * h, y[n - 1] + h * k3)
        y.append(y[n - 1] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4))

    return y
