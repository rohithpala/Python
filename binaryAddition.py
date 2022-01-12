bin1 = input("Enter Binary Number 1: ")
bin2 = input("Enter Binary Number 2: ")

len1 = len(bin1)
len2 = len(bin2)

if len1 > len2:
    bin2 = bin2.rjust(len1, "0")
else:
    bin1 = bin1.rjust(len2, "0")

s = ""
carry = 0
for i in range(len1 - 1, -1, -1):
    sod = int(bin1[i]) + int(bin2[i])  # sum of digits
    carry = 0
    if sod > 1:
        carry = 1
        s += "0"
    else:
        s += str(sod)

s = s[::-1]

if carry == 1:
    s = "1" + s

print("Sum:", s)
