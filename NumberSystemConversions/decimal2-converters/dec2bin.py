try:
    decimal = int(input("Enter Decimal Number: "))
    binary = ""

    while decimal > 0:
        binary += str(decimal % 2)
        decimal //= 2

    binary = binary[::-1]
    print("Binary Form:", binary)
except ValueError:
    print("Invalid Decimal Form")
