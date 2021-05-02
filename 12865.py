import sys
n,k = map(int, sys.stdin.readline().split())
arr = [(0,0)]+[tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for w in range(1,k+1):
        if w >= arr[i][0]:
            dp[i][w] = max(dp[i-1][w],dp[i-1][w-arr[i][0]] + arr[i][1]) # 택한 경우
        else : 
            dp[i][w] = dp[i-1][w] # 택하지 않는 경우
print(dp[n][k])