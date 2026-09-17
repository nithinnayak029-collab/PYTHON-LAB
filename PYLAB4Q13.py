import numpy as np
from scipy.integrate import quad

f = lambda x: np.sin(x) + x**2
x = 2
a, b = 0, 1

derivative = (f(x + 1e-5) - f(x - 1e-5)) / (2e-5)
integral, error = quad(f, a, b)

print("Derivative at x =", x, ":", derivative)
print("Integral from", a, "to", b, ":", integral)