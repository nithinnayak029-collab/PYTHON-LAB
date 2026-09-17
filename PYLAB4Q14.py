import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([6, 17, 34, 57, 86, 121])

def f(x, a, b, c):
    return a*x**2 + b*x + c

p, _ = curve_fit(f, x, y)

print("a =", p[0])
print("b =", p[1])
print("c =", p[2])

xx = np.linspace(1, 6, 100)

plt.scatter(x, y, color="red", label="Data points")
plt.plot(xx, f(xx, *p), color="blue", label="Fitted curve")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()