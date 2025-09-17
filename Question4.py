import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(legacy='1.25')
# np.set_printoptions(precision=8)


def f(x, y):
    return -8 * y + 6 * np.exp(-2 * x)


def ye(x):
    return np.exp(-2 * x) - np.exp(-8 * x)


def forwardEuler(y0, x0, h, N):
    y = [y0]
    for n in range(1, N + 1):
        y.append(y[n - 1] + h * f(x0 + (n - 1) * h, y[n - 1]))
    return y


def AB2(y0, x0, h, N):
    y = forwardEuler(y0, x0, h, 1)
    for n in range(2, N + 1):
        y.append(y[n - 1] + h * (1.5 * f(x0 + h * (n - 1), y[n - 1]) - 0.5 * f(x0 + h * (n - 2), y[n - 2])))

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


def globalErrors(y, x0, h):
    En = []
    for i in range(len(y)):
        En.append(y[i] - ye(x0 + i * h))
    return En


y1 = forwardEuler(0, 0, 0.08, int(2 / 0.08))
y2 = AB2(0, 0, 0.08, int(2 / 0.08))
y3 = RK4(0, 0, 0.08, int(2 / 0.08))

Ens1 = []
Ens2 = []
Ens3 = []

for k in range(16):
    y = forwardEuler(0, 0, 0.16 / (2 ** k), 2 ** k)
    Ens1.append(y[len(y) - 1] - ye(0.16))

for k in range(16):
    y = AB2(0, 0, 0.16 / (2 ** k), 2 ** k)
    Ens2.append(y[len(y) - 1] - ye(0.16))

for k in range(16):
    y = RK4(0, 0, 0.16 / (2 ** k), 2 ** k)
    Ens3.append(y[len(y) - 1] - ye(0.16))


k = np.linspace(0, 15, num=16)

lnh = np.log(0.16/(2**k))

print(Ens3)
print(np.log(np.abs(Ens3)))

plt.scatter(lnh, np.log(np.abs(Ens1)))
plt.scatter(lnh, np.log(np.abs(Ens2)))
plt.scatter(lnh, np.log(np.abs(Ens3)))
plt.legend(["Forward Euler","AB2","RK4"])
plt.xlabel("ln(h)")
plt.ylabel("ln|E_n|")
plt.show()
