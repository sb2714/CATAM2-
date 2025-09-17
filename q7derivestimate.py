import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True

alpha = 2


def f(x, y, z):
    return z


def g(x, y, z, p):
    return - np.power(p, 2) * y / np.power(1 + x, alpha)


def RK4(y0, x0, h, N, p):
    y = [y0]
    for n in range(1, N + 1):
        k1 = [f(x0 + (n - 1) * h, y[n - 1][0], y[n - 1][1]), g(x0 + (n - 1) * h, y[n - 1][0], y[n - 1][1], p)]
        k2 = [f(x0 + (n - 0.5) * h, y[n - 1][0] + 0.5 * h * k1[0], y[n - 1][1] + 0.5 * h * k1[1]),
              g(x0 + (n - 0.5) * h, y[n - 1][0] + 0.5 * h * k1[0], y[n - 1][1] + 0.5 * h * k1[1], p)]
        k3 = [f(x0 + (n - 0.5) * h, y[n - 1][0] + 0.5 * h * k2[0], y[n - 1][1] + 0.5 * h * k2[1]),
              g(x0 + (n - 0.5) * h, y[n - 1][0] + 0.5 * h * k2[0], y[n - 1][1] + 0.5 * h * k2[1], p)]
        k4 = [f(x0 + n * h, y[n - 1][0] + h * k3[0], y[n - 1][1] + h * k3[1]),
              g(x0 + n * h, y[n - 1][0] + h * k3[0], y[n - 1][1] + h * k3[1], p)]
        y.append([y[n - 1][0] + (h / 6) * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]),
                  y[n - 1][1] + (h / 6) * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])])

    return y


a = [0, 1]
h = 1/(20)
print(h)
epsilon = 10**(-7)
print(epsilon)


k = 1

p = np.linspace(0,20, num=1000)
y = RK4(a, 0, h, int(1 / h), p)[int(1 / h)][0]

plt.plot(p,y)
plt.xlabel('p')
plt.ylabel('Ø(p)')
plt.show()

