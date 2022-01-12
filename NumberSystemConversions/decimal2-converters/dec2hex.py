try:
    decimal = int(input("Enter Decimal Number: "))

    HEX_CHARACTERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    hexadecimal = ""

    while decimal > 0:
        hexadecimal += HEX_CHARACTERS[decimal % 16]
        decimal //= 16

    hexadecimal = hexadecimal[::-1]
    print("Hexadecimal Form:", hexadecimal)
except ValueError:
    print("Invalid Decimal Form")
