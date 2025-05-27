import numpy as np


A = np.random.randint(1, 20, size=(4, 4))
B = np.eye(4, dtype=int)

print("Matrix A:\n", A)
print("Matrix B:\n", B)

print("A - B =\n", A - B)

avg = (A.sum() + B.sum()) / (A.size + B.size)
print("Average of all elements in A and B:", avg)

print("Min value in A:", A.min())

A_reshaped = A.reshape(2, 8)
B_reshaped = B.reshape(8, 2)
print("Reshaped A:\n", A_reshaped)
print("Reshaped B:\n", B_reshaped)
print("Multiplication (reshaped):\n", np.matmul(A_reshaped, B_reshaped))

col1_sum = A[:, 0].sum()
row4_sum = B[3, :].sum()
print("Sum of A's 1st column and B's 4th row:", col1_sum + row4_sum)

A_mod = A.copy()
A_mod[:, 2] = A[:, 2] * 2
print("A with 3rd column doubled:\n", A_mod)

vert_join = np.vstack((A, B))
print("Vertically joined A and B:\n", vert_join)

A_float = A.astype(float)
B_float = B.astype(float)
print("A + B as floats:\n", A_float + B_float)
