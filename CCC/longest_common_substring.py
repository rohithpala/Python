def f(s1, n1, s2, n2):
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    maximum = 0
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0
            maximum = max(maximum, dp[i][j])
    return maximum

n1 = int(input())
s1 = ''.join(input().split())
n2 = int(input())
s2 = ''.join(input().split())
print(f(s1, n1, s2, n2))