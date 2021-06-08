import sys
n = int(sys.stdin.readline())
price = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0] = price[0]
for i in range(1,n):
    dp[i][0] = dp[i-1][0] + price[i][0]
    dp[i][i] = dp[i-1][i-1]+ price[i][i]
    for j in range(1,i):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + price[i][j]

print(max(dp[n-1]))