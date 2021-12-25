def swap_case(s):
    res = ""
    for ch in s:
        if ch.isalpha():
            res += ch.lower() if ch.isupper() else ch.upper()
        else:
            res += ch
    return res


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
