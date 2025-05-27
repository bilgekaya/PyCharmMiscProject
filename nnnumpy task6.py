import numpy as np

A = np.random.randint(0, 10, size=(4, 4))
B = np.identity(4, dtype=int)

print("Matrix A:\n", A)
print("Matrix B:\n", B)

print("A + B =\n", A + B)

print("Sum of all elements in A and B:", A.sum() + B.sum())

print("Max value in A:", A.max())

A_reshaped = A.reshape(8, 2)
B_reshaped = B.reshape(2, 8)
print("A reshaped:\n", A_reshaped)
print("B reshaped:\n", B_reshaped)
print("A x B =\n", np.matmul(A_reshaped, B_reshaped))

print("Sum of A's 3rd column and B's 3rd row:", A[:, 2].sum() + B[2, :].sum())

A_modified = A.copy()
A_modified[:, 1] = A[:, 1] ** 2
print("A with 2nd column squared:\n", A_modified)

joined = np.hstack((A, B))
print("Horizontally joined A and B:\n", joined)

#
