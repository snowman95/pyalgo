import sys

n = int(sys.stdin.readline())
price = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
dp = [[0]*3 for _ in range(n)]
dp[0] = price[0]

for i in range(1,n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + price[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + price[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + price[i][2]
print(min(dp[n-1]))