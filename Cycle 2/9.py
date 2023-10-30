import numpy as np
print("University No: SJC22MCA-2021 \nName: Christin Benny \nBatch: S3 MCA \n______________________________________\n")
A = np.array([1, 2, 3, 4, 5])


D = np.diag(A)


print("Original 1D Array:")
print(A)

print("\nDiagonal Matrix:")
print(D)

B = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

D_square = np.diag(B)

print("\nOriginal Square Matrix:")
print(B)

print("\nDiagonal Elements:")
print(D_square)

C = np.array([[1, 2, 3],
              [4, 5, 6]])

D_nonsquare = np.diag(C)


print("\nOriginal Non-Square Matrix:")
print(C)

print("\nDiagonal Matrix from Non-Square Matrix:")
print(D_nonsquare)
