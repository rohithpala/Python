from math import pow
from re import findall

octal = input("Enter Octal Form: ").upper()

if len(findall("^[0-7]*$", octal)):
    l = len(octal)

    decimal = 0

    for i in range(l):
        decimal += int(octal[l - i - 1]) * pow(8, float(i))

    print("Decimal Form:", int(decimal))
else:
    print("Invalid Octal Form")
