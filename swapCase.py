def swapCase(s):
    result = ""
    for ch in s:
        if ch.isalpha():
            result += ch.lower() if ch.isupper() else ch.upper()
        else:
            result += ch
    return result


if __name__ == "__main__":
    s = input("Enter a Word/Sentene")
    result = swapCase(s)
    print(result)
