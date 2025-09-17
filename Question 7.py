import numpy as np

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


n = 0
a = [0, 1]
h = 0.01
print(h)
epsilon = 10**(-7)
print(epsilon)

def falsePos(p1, p2):
    a = [0, 1]
    pp1 = RK4(a, 0, h, int(1 / h), p1)[int(1 / h)][0]
    a = [0, 1]
    pp2 = RK4(a, 0, h, int(1 / h), p2)[int(1 / h)][0]
    p = (pp2 * p1 - pp1 * p2) / (pp2 - pp1)
    a = [0, 1]
    print(", ", p1,", ", p2, ", ",p, ", ", abs(p - np.sqrt(0.25 + (np.pi / np.log(2))**2)))
    if abs(RK4(a, 0, h, int(1 / h), p)[int(1 / h)][0]) < epsilon:
        return p
        print(p)
    else:
        if p1 * p < 0:
            return falsePos(p1, p)
        return falsePos(p, p2)


print(falsePos(4, 5))
