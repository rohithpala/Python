def min_no_of_operations(a, n1, b, n2):
     dp = [[0 for _ in range(n1)] for _ in range(n2)]
     for i in range(n1+1):
          for j in range(n2+1):
               print(i, j)
               if i == 0:
                    dp[0][j] = j
               elif j == 0:
                    dp[i][0] = i
               else:
                    if a[i-1] == b[j-1]:
                         dp[i][j] = dp[i-1][j-1]
                    else:
                         dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
     return dp[n1][n2]

n1 = int(input())
a = 'c' + ''.join(input().split())
n2 = int(input())
b = 'c' + ''.join(input().split())
print(min_no_of_operations(a, n1+1, b, n2+1))