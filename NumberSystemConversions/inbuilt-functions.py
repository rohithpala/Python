decimal = int(input("Enter a Decimal Number: "))

print("Binary Form:      ", bin(decimal)[2:])
print("Octal Form:       ", oct(decimal)[2:])
print("Hexadecimal Form: ", hex(decimal)[2:].upper())

binary = input("Enter a Binary Number: ")
value = int(binary, 2)

print("Decimal Form:     ", value)
print("Octal Form:       ", oct(value)[2:])
print("Hexadecimal Form: ", hex(value)[2:].upper())

octal = input("Enter a Octal Number: ")
value = int(octal, 8)

print("Binary Form:      ", bin(value)[2:])
print("Decimal Form:     ", value)
print("Hexadecimal Form: ", hex(value)[2:].upper())

hexadecimal = input("Enter a Hexadecimal Number: ")
value = int(hexadecimal, 16)

print("Binary Form:  ", bin(value)[2:])
print("Decimal Form: ", value)
print("Octal Form:   ", oct(value)[2:])
