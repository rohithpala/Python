# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000942404

t = int(input())
for T in range(1, t+1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    print("Case #" + str(T) + ": " + str(sum(lst)%m))
