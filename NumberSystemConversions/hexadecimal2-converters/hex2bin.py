from re import findall

hexadecimal = input("Enter Hexadecimal Form: ").upper()

if findall("^[0-9A-F]*$", hexadecimal):
    HEX2BIN = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }

    print("Binary Form: ", end="")
    for character in hexadecimal:
        print(HEX2BIN[character], end="")
else:
    print("Invalid Hexadecimal Form")
