from math import pow

binary = input("Enter Binary Form: ")

test = set(binary)
if test == {"0", "1"} or test == {"0"} or test == {"1"}:
    l = len(binary)
    decimal = 0

    for i in range(l):
        decimal += int(binary[l - i - 1]) * pow(2, float(i))

    print("Decimal Form:", int(decimal))
else:
    print("Invalid Binary Form")
