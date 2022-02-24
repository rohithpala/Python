# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000941ec5
def ruledBy(kingdom):
    char = kingdom[-1].lower()
    if char == "y":
        return "nobody"
    elif char in ("a", "e", "i", "o", "u"):
        return "Alice"
    return "Bob"

t = int(input())
for T in range(1, t+1):
    kingdom = input()
    print("Case #" + str(T) + ": " + kingdom + " is ruled by " + ruledBy(kingdom) + ".")
