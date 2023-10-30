import numpy as np

print("University No: SJC22MCA-2021 \nName: Christin Benny \nBatch: S3 MCA \n______________________________________\n")

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])


U, S, VT = np.linalg.svd(A)


reconstructed_A = np.dot(U, np.dot(np.diag(S), VT))

print("Original Matrix A:")
print(A)

print("\nMatrix U:")
print(U)

print("\nSingular Values S:")
print(S)

print("\nMatrix VT (Transpose of V):")
print(VT)

print("\nSVD Reconstructed Matrix A:")
print(reconstructed_A)
