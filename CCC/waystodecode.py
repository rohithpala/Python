def decode(s, l):
     if l == 2 or l == 3:
          return l-1

     ways = [1]*(l)
     m = 10**9 + 7
     for i in range(2, l):
          num = int(s[i-1] + s[i])
          if 0 <= num <= 25:
               ways[i] = ways[i-1]%m + ways[i-2]%m
          else:
               ways[i] = ways[i-1]%m
     return ways[l-1]%m

s = "c" + input()
print(decode(s, len(s)))
