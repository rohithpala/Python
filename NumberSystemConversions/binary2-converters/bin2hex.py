from re import findall

binary = input("Enter Binary Form: ")

if findall("^[01]*$", binary):
    l = len(binary)

    BIN2HEX = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"
    }

    mod = l % 4
    padding = 4 - mod if mod != 0 else 0

    binary = binary.rjust(l + padding, "0")
    chunks = [binary[i : i + 4] for i in range(0, l, 4)]

    print("Hexadecimal Form: ", end="")
    for chunk in chunks:
        print(BIN2HEX[chunk], end="")
else:
    print("Invalid Binary Form")
