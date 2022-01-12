from re import findall

binary = input("Enter Binary Form: ")

if findall("^[01]*$", binary):
    l = len(binary)

    BIN2OCT = {
        "000": "0",
        "001": "1",
        "010": "2",
        "011": "3",
        "100": "4",
        "101": "5",
        "110": "6",
        "111": "7"
    }

    mod = l % 3
    padding = 3 - mod if mod != 0 else 0

    binary = binary.rjust(l + padding, "0")
    chunks = [binary[i : i + 3] for i in range(0, l, 3)]

    print("Octal Form: ", end="")
    for chunk in chunks:
        print(BIN2OCT[chunk], end="")
else:
    print("Invalid Binary Form")
