from re import findall

def bin2hex(binary):
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
        "1111": "F",
    }

    mod = l % 4
    padding = 4 - mod if mod != 0 else 0

    binary = binary.rjust(l + padding, "0")
    chunks = [binary[i : i + 4] for i in range(0, l, 4)]

    octal = ""
    for chunk in chunks:
        octal += BIN2HEX[chunk]
    return octal


def oct2bin(octal):
    l = len(octal)
    OCT2BIN = {
        "0": "000",
        "1": "001",
        "2": "010",
        "3": "011",
        "4": "100",
        "5": "101",
        "6": "110",
        "7": "111",
    }

    binary = ""
    for character in octal:
        binary += OCT2BIN[character]
    return binary


if __name__ == "__main__":
    octal = input("Enter Octal Form: ")

    if findall("^[0-9A-F]*$", octal):
        hexadecimal = bin2hex(oct2bin(octal))
        print("Hexadecimal Form:", hexadecimal)  # .lstrip("0"))
    else:
        print("Invalid Octal Form")
