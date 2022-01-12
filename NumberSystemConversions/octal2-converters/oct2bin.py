from re import findall

octal = input("Enter Octal Form: ")

if findall("^[0-9A-F]*$", octal):
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

    print("Octal Form: ", end="")
    for character in octal:
        print(OCT2BIN[character], end="")
else:
    print("Invalid Octal Form")
