import numpy as np

print("University No: SJC22MCA-2021 \nName: Christin Benny \nBatch: S3 MCA \n______________________________________\n")

even_numbers = np.arange(2, 32, 2)
print(even_numbers)

elements_from_2_to_8_step_2 = even_numbers[2:9:2]

print("a. Elements from index 2 to 8 with step 2:", elements_from_2_to_8_step_2)

last_3_elements = even_numbers[-3:]

print("b. Last 3 elements of the array using negative index:", last_3_elements)

alternate_elements = even_numbers[::2]

print("c. Alternate elements of the array:", alternate_elements)

last_3_alternate_elements = even_numbers[-1::-2][:3]

print("d. Last 3 alternate elements of the array:", last_3_alternate_elements)

