print("University No: SJC22MCA-2021 \nName: Christin Benny \nBatch: S3 MCA \n______________________________________\n")
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def are_coprime(num1, num2):
    return gcd(num1, num2) == 1

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if are_coprime(num1, num2):
    print(f"{num1} and {num2} are coprime.")
else:
    print(f"{num1} and {num2} are not coprime.")