bin1 = input("Enter Binary Number 1: ")
bin2 = input("Enter Binary Number 2: ")

l1 = len(bin1)
l2 = len(bin2)

if l1 > l2:
    bin2 = bin2.rjust(l1, "0")
else:
    bin1 = bin1.rjust(l2, "0")

s = ""
carry = 0
for i in range(l1 - 1, -1, -1):
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
