from math import pow
from re import findall

binary = input("Enter Binary Form: ")

if findall("^[01]*$", binary):
    l = len(binary)
    decimal = 0

    for i in range(l):
        decimal += int(binary[l - i - 1]) * pow(2, float(i))

    print("Decimal Form:", int(decimal))
else:
    print("Invalid Binary Form")
