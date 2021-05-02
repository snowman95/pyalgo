import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
for i in range(n):
    dp[i] = max(dp[i-1]+ arr[i], arr[i])
print(max(dp))