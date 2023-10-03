print("University No: SJC22MCA-2021 \nName: Christin Benny \nBatch: S3 MCA \n______________________________________\n")
print("Enter the lengths of the triangle sides: ")
s1 = int(input("s1: "))
s2 = int(input("s2: "))
s3 = int(input("s3: "))

if s1 == s2 == s3:
    print("It is an Equilateral triangle")
elif s1 == s2 or s2 == s3 or s3 == s1:
    print("It is an Isosceles triangle")
else:
    print("It is a Scalene triangle")