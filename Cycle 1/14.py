print("University No: SJC22MCA-2021 \nName: Christin Benny \nBatch: S3 MCA \n______________________________________\n")
def find_absent_digits(mobile_number):

    all_digits = set("0123456789")


    number_digits = set(mobile_number)


    absent_digits = all_digits - number_digits

    return absent_digits



mobile_number = input("Enter a 10-digit mobile number: ")


if len(mobile_number) == 10 and mobile_number.isdigit():

    absent_digits = find_absent_digits(mobile_number)

    if absent_digits:
        print("Absent digits:", ', '.join(absent_digits))
    else:
        print("All digits are present in the mobile number.")
else:
    print("Invalid input. Please enter a 10-digit mobile number.")
