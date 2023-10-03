print("University No: SJC22MCA-2021 \nName: Christin Benny \nBatch: S3 MCA \n______________________________________\n")
def is_prime(num):
    if num <= 1:
        return False
    for i in range (2,num):
        if num % i == 0:
            return False
    return True
f=int(input("Enter the starting number: "))
l=int(input("Enter the end number: "))
print("non-prime numbers are: ")
for num in range(f,l+1):
    if not is_prime(num):
        print(num,end=" ")