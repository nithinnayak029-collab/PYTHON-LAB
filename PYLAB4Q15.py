from scipy.optimize import minimize

def f(x):
    return (x[0] - 2)**2 + (x[1] - 2)**2

result = minimize(f, [0, 0], method='BFGS')

print("Minimum value:", result.fun)
print("At x =", result.x[0])
print("At y =", result.x[1])