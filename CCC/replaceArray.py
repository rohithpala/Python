n = int(input())
a = list(map(int, input().split()))
m = k = a[n - 1]
a[n - 1] = 0
for i in range(n - 2, -1, -1):
     m = max(m, k)
     k = a[i]
     a[i] = m

for num in a:
    print(num, end=" ")
