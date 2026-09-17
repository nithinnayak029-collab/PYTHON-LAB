# Matrix Operations using NumPy and without NumPy

import numpy as np

# Matrices
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

print("========== USING NUMPY ==========")

# Convert lists to NumPy arrays
A_np = np.array(A)
B_np = np.array(B)

print("\nMatrix A:")
print(A_np)

print("\nMatrix B:")
print(B_np)

# Addition
print("\nAddition:")
print(A_np + B_np)

# Subtraction
print("\nSubtraction:")
print(A_np - B_np)

# Multiplication
print("\nMultiplication:")
print(np.dot(A_np, B_np))

# Transpose
print("\nTranspose of A:")
print(A_np.T)

print("\nTranspose of B:")
print(B_np.T)


print("\n========== WITHOUT NUMPY ==========")

# Addition
def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


# Subtraction
def subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


# Multiplication
def multiply(A, B):
    result = [[0 for j in range(len(B[0]))]
              for i in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


# Transpose
def transpose(A):
    return [[A[j][i] for j in range(len(A))]
            for i in range(len(A[0]))]


print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nAddition:")
print(add(A, B))

print("\nSubtraction:")
print(subtract(A, B))

print("\nMultiplication:")
print(multiply(A, B))

print("\nTranspose of A:")
print(transpose(A))

print("\nTranspose of B:")
print(transpose(B))