import numpy as np

np.set_printoptions(legacy='1.25')

h0 = [.5, 0.375, 0.25, 0.125, 0.1, 0.05, 0.000001]


def f(x, y):
    return -8 * y + 6 * np.exp(-2 * x)


def ye(x):
    return np.exp(-2 * x) - np.exp(-8 * x)


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


def globalErrors(y, x0, h):
    En = []
    for i in range(len(y)):
        En.append(y[i] - ye(x0 + i * h))
    return En


def analyticSolution(x0, h, N):
    yes = []
    for n in range(N + 1):
        yes.append(ye(x0 + n * h))
    return yes


for h in h0:

    Y = AB2(float(0), float(0), h, 6)
    Y_e = analyticSolution(float(0), h, 6)
    En = globalErrors(Y, float(0), h)

    print(Y)
    print(Y_e)
    print(En)

    for i in range(2, len(En)):
        print(abs(En[i]) / abs(En[i - 1]))

    gamma = np.log(abs(En[len(En) - 1] / En[len(En) - 2])) / h

    print(gamma , " : h  " , h)
