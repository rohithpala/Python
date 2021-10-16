# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b3771
T = int(input())
for t in range(T):
    n, d, c, m = input().split()
    n, d, c, m = int(n), int(d), int(c), int(m)
    s = input()
    if s.count('C') == len(s):
        print("Case #" + str(t+1) + ": YES")
    else:
        s = s[:s.rindex('D', 0, len(s))+1]
        dogs = s.count('D')
        yes = True
        for i in s:
             if d != 0:
               if i == 'D':
                    d -= 1
                    c += m
               else:
                    c -= 1
             else:
                  yes = False
                  break
        if yes:
             print("Case #" + str(t+1) + ": YES")
        else:
             print("Case #" + str(t+1) + ": NO")
     #    if s.count('D') <= d and s.count('C') <= (c+m):
     #        print("Case #" + str(t+1) + ": YES")
     #    else:
     #        print("Case #" + str(t+1) + ": NO")