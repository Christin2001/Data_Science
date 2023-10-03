print("University No: SJC22MCA-2021 \nName: Christin Benny \nBatch: S3 MCA \n______________________________________\n")
num=int(input("enter the  range:"))
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()