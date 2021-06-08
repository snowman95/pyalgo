import sys
n = int(sys.stdin.readline())
price = [int(sys.stdin.readline()) for _ in range(n)]
dp = [[0]*2  for _ in range(n+1)]

dp[0][0] = price[0]
dp[0][1] = price[0]

if n>=2:
    dp[1][0] = price[1]
    dp[1][1] = dp[0][1] + price[1]

# dp[i][0] : 이 계단을 밟으면 1칸 연속 (2단 점)
# dp[i][1] : 이 계단을 밟으면 2칸 연속 (1단 점)
for i in range(2,n):
    dp[i][0] = max(dp[i-2]) + price[i]
    dp[i][1] = dp[i-1][0] + price[i]

print(max(dp[n-1]))