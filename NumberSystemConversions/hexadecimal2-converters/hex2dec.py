from math import pow
from re import findall

hexadecimal = input("Enter Hexadecimal Form: ").upper()

if len(findall("^[0-9A-F]*$", hexadecimal)):
    l = len(hexadecimal)
    HEX2DEC = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

    decimal = 0

    for i in range(l):
        character = hexadecimal[l - i - 1]
        if character.isdigit():
            decimal += int(character) * pow(16, float(i))
        else:
            decimal += int(HEX2DEC[character]) * pow(16, float(i))

    print("Decimal Form:", int(decimal))
else:
    print("Invalid Hexadecimal Form")
