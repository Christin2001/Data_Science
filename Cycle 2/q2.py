import numpy as np
print("University No: SJC22MCA-2021 \nName: Christin Benny \nBatch: S3 MCA \n______________________________________\n")
complex_array = np.array([
    [1 + 2j, 2 + 3j, 3 + 4j],
    [4 + 5j, 5 + 6j, 6 + 7j]
], dtype=complex)

print("2D Array:")
print(complex_array)

rows, columns = complex_array.shape

print("Number of rows:", rows)
print("Number of columns:", columns)

print("Array dimension:", complex_array.shape)

reshaped_array = complex_array.reshape(3, 2)

print("Reshaped 3x2 Array:")
print(reshaped_array)
