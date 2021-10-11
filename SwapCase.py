def swap_case(s):
    res = ""
    for ch in s:
        if ch.isalpha():
            if ch.isupper():
                res += ch.lower()
            else:
                res += ch.upper()
        else:
            res += ch
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
