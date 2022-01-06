from re import findall

def bin2oct(binary):
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

    l = len(binary)
    mod = l % 3
    padding = 3 - mod if mod != 0 else 0

    binary = binary.rjust(l + padding, "0")
    chunks = [binary[i : i + 3] for i in range(0, l, 3)]

    octal = ""
    for chunk in chunks:
        octal += BIN2OCT[chunk]
    return octal


def hex2bin(hexadecimal):
    l = len(hexadecimal)
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
    binary = ""
    for character in hexadecimal:
        binary += HEX2BIN[character]
    return binary


if __name__ == "__main__":
    hexadecimal = input("Enter Hexadecimal Form: ").upper()

    if findall("^[0-9A-F]*$", hexadecimal):
        octal = bin2oct(hex2bin(hexadecimal))
        print("Octal Form:", octal.lstrip("0"))
    else:
        print("Invalid Hexadecimal Form")
