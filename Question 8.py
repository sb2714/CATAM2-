import matplotlib.pyplot as plt
import numpy as np

alpha = 10


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


n = 0
a = [0, 1]
h = 0.001
print(h)
epsilon = 10 ** (-10)
print(epsilon)


def normalisation(x, y, p):
    y2 = []
    for i in range(len(y)):
        y2.append((p ** 2) * (y[i] ** 2) / ((1 + x[i]) ** 10))
    y2 = np.array(y2)
    return np.trapezoid(y2, x)


def falsePos(p1, p2):
    a = [0, 1]
    pp1 = RK4(a, 0, h, int(1 / h), p1)[int(1 / h)][0]
    a = [0, 1]
    pp2 = RK4(a, 0, h, int(1 / h), p2)[int(1 / h)][0]
    p = (pp2 * p1 - pp1 * p2) / (pp2 - pp1)
    a = [0, 1]
    print(", ", p1, ", ", p2, ", ", p, ", ", abs(p - np.sqrt(0.25 + (np.pi / np.log(2)) ** 2)))
    if abs(RK4(a, 0, h, int(1 / h), p)[int(1 / h)][0]) < epsilon:
        return p
        print(p)
    else:
        if p1 * p < 0:
            return falsePos(p1, p)
        return falsePos(p, p2)


first = [0, 15, 30, 45, 55, 68]
second = [15, 30, 45, 55, 68, 80]
p = [falsePos(0, 15), falsePos(15, 30), falsePos(30, 45), falsePos(45, 55), falsePos(55, 68), falsePos(68, 80)]
print(p)

for i in range(len(p)):
    print(str(i + 1), ", ", p[i], ", ", first[i], ", ", second[i])

fig, axs = plt.subplots(2, 3)

for i in range(len(p)):
    x = np.linspace(0, 1, num=int(1 / h) + 1)
    print(x)
    y1 = RK4([0, 1], 0, h, int(1 / h), p[i])
    y2 = []
    for y in y1:
        y2.append(y[0])
    k = 1 / np.sqrt(normalisation(x, y2, p[i]))
    print(y2)
    axs[int(i / 3), i % 3].plot(x, k * np.array(y2))
    axs[int(i / 3), i % 3].set_title("k = " + str(i + 1))
    axs[int(i / 3), i % 3].set_xlabel("x")
    axs[int(i / 3), i % 3].set_ylabel("y^(" + str(i + 1) + ")")
plt.show()
