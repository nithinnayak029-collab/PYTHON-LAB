import numpy as np

A = np.array ([[2,4],[1,2]])
B = np.array ([[7,3],[6,4]])
print("Array of A ",A)
print("Array of B ",B)
C = np.linalg.det(A)
D = np.linalg.det(B)

print("Determinant of A ",C)
print("Determinant of B ",D)

if C != 0:
    print("Rank of A is 2")
    E = np.linalg.inv(A)
    print("Inverse of A ",E)
else:
    print("Rank is 1")
  
if D != 0:
    print("Rank of B is 2")
    F = np.linalg.inv(B)
    print("Inverse of B ",F)
else:
    print("Rank is 1")