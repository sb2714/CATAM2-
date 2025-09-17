import numpy as np
import matplotlib.pyplot as plt

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

y1 = forwardEuler(0,0,0.08, int(2/0.08))
print(2/0.08)
y2 = AB2(0,0,0.08,int(2/0.08))
y3 = RK4(0,0,0.08,int(2/0.08))

print(y2)


fig, axs = plt.subplots(1,3)

xinf = np.linspace(0,2,num=100000)
ye = np.exp(-2*xinf) - np.exp(-8*xinf)
x = np.linspace(0,2,num= int(2/0.08) + 1)
print(x)
axs[0].scatter(x,y1, color='g')
axs[0].plot(xinf,ye)
axs[1].scatter(x,y2, color='b')
axs[1].plot(xinf,ye)
axs[2].scatter(x,y3, color='r')
axs[2].plot(xinf,ye)

axs[0].set_title("Forward Euler")
axs[0].set_xlabel("x")
axs[0].set_ylabel("Y_n,y_e")
axs[0].legend(["Y_n", "y_e"])

axs[1].set_title("AB2")
axs[1].set_xlabel("x")
axs[1].set_ylabel("Y_n,y_e")
axs[1].legend(["Y_n", "y_e"])

axs[2].set_title("RK4")
axs[2].set_xlabel("x")
axs[2].set_ylabel("Y_n,y_e")
axs[2].legend(["Y_n", "y_e"])



plt.show()