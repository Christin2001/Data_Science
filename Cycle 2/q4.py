import numpy as np

print("University No: SJC22MCA-2021 \nName: Christin Benny \nBatch: S3 MCA \n______________________________________\n")

one_dimensional_array = np.arange(10)

first_4_elements = one_dimensional_array[:4]

last_6_elements = one_dimensional_array[-6:]

elements_2_to_7 = one_dimensional_array[2:8]

print("Original Array:", one_dimensional_array)
print("a. First 4 elements:", first_4_elements)
print("b. Last 6 elements:", last_6_elements)
print("c. Elements from index 2 to 7:", elements_2_to_7)
