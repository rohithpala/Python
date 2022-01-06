try:
    decimal = int(input("Enter Decimal Number: "))

    octal = ""

    while decimal > 0:
        octal += str(decimal % 8)
        decimal //= 8

    octal = octal[::-1]
    print("Octal Form:", octal)
except ValueError:
    print("Invalid Decimal Form")
