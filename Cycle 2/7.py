import numpy as np
print("University No: SJC22MCA-2021 \nName: Christin Benny \nBatch: S3 MCA \n______________________________________\n")

matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

addition_result = matrix1 + matrix2
print("a. Addition Result:")
print(addition_result)

subtraction_result = matrix1 - matrix2
print("b. Subtraction Result:")
print(subtraction_result)

multiplication_result = matrix1 * matrix2
print("c. Multiplication Result:")
print(multiplication_result)

epsilon = 1e-15
division_result = np.divide(matrix1, matrix2 + epsilon)
print("d. Division Result:")
print(division_result)

matrix_multiplication_result = np.dot(matrix1, matrix2)
print("e. Matrix Multiplication Result:")
print(matrix_multiplication_result)

transpose_result = np.transpose(matrix1)
print("f. Transpose of the Matrix:")
print(transpose_result)

diagonal_sum = np.trace(matrix1)
print("g. Sum of Diagonal Elements:")
print(diagonal_sum)
