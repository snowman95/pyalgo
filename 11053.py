import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1]*n
for cur in range(1, n):
    for front in range(0, cur):
        if arr[front] < arr[cur]:
            dp[cur] = max(dp[cur], dp[front]+1)
print(max(dp))