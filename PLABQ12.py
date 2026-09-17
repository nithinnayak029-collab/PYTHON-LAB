import numpy as np

# Define the matrix
A = np.array([[4, 2],
              [1, 3]])

print("Matrix A:")
print(A)

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Display eigenvalues
print("\nEigenvalues:")
print(eigenvalues)

# Display eigenvectors
print("\nEigenvectors:")
print(eigenvectors)

# Display each eigenvalue with its corresponding eigenvector
print("\nEigenvalue and corresponding Eigenvector:")

for i in range(len(eigenvalues)):
    print("\nEigenvalue:", eigenvalues[i])
    print("Eigenvector:", eigenvectors[:, i])