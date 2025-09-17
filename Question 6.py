import matplotlib.pyplot as plt
import numpy as np

p = 5
alpha = 2

def ye(x):
    return 2 * np.sqrt(x + 1) * np.sin(np.log(x + 1) * np.sqrt(4*(p**2) - 1) / 2) / np.sqrt(4*(p**2) - 1)

def f(x, y, z):
    return z


def g(x, y, z):
    return - np.power(p, 2) * y / np.power(1 + x, alpha)


def RK4(y0, x0, h, N):
    y = [y0]
    for n in range(1, N + 1):
        k1 = [f(x0 + (n - 1) * h, y[n - 1][0], y[n - 1][1]), g(x0 + (n - 1) * h, y[n - 1][0], y[n - 1][1])]
        k2 = [f(x0 + (n - 0.5) * h, y[n - 1][0] + 0.5 * h * k1[0], y[n - 1][1] + 0.5 * h * k1[1]),
              g(x0 + (n - 0.5) * h, y[n - 1][0] + 0.5 * h * k1[0], y[n - 1][1] + 0.5 * h * k1[1])]
        k3 = [f(x0 + (n - 0.5) * h, y[n - 1][0] + 0.5 * h * k2[0], y[n - 1][1] + 0.5 * h * k2[1]),
              g(x0 + (n - 0.5) * h, y[n - 1][0] + 0.5 * h * k2[0], y[n - 1][1] + 0.5 * h * k2[1])]
        k4 = [f(x0 + n * h, y[n - 1][0] + h * k3[0], y[n - 1][1] + h * k3[1]),
              g(x0 + n * h, y[n - 1][0] + h * k3[0], y[n - 1][1] + h * k3[1])]
        y.append([y[n - 1][0] + (h / 6) * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]),
                  y[n - 1][1] + (h / 6) * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])])

    return y


a = [0, 1]
things = []
for k in range(13):
    Y = RK4(a, 0, 0.1 / (2 ** k), 10 * (2 ** k))
    print(k, ", $2^{"+ str(k)+ "}$, ", Y[10 * (2 ** k)][0], ", ", Y[10 * (2 ** k)][0] - ye(1))
    things.append((Y[10 * (2 ** k)][0] - ye(1))*(10**5)/(2**(5*k)))
    print((Y[10 * (2 ** k)][0] - ye(1))*(10**5)/(2**(5*k)))

k = np.linspace(0,12,num=13)
plt.scatter(np.log(10*np.power(2,k)),np.log(np.abs(things)))
plt.xlabel("ln(h) = 10 + kln(2)")
plt.ylabel("ln|e_n|")
plt.show()
