import pandas as pd
print("University No: SJC22MCA-2021 \nName: Christin Benny \nBatch: S3 MCA \n______________________________________\n")
iris_df = pd.read_csv('iris.csv')

shape = iris_df.shape
print("Shape of the data set:", shape)


first_5_rows = iris_df.head()
last_5_rows = iris_df.tail()
print("\nFirst 5 rows:\n", first_5_rows)
print("\nLast 5 rows:\n", last_5_rows)

size = iris_df.size
print("\nSize of the dataset:", size)

sample_counts = iris_df['variety'].value_counts()
print("\nNumber of samples available for each variety:\n", sample_counts)

description = iris_df.describe()
print("\nDescription of the dataset:\n", description)
