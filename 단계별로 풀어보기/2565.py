import sys
n = int(sys.stdin.readline())

arr = []
dp = [1]*n
for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    arr.append((x,y))

arr.sort()
for cur in range(n):
    for pre in range(0, cur):
        if arr[pre][1] < arr[cur][1]:
            dp[cur] = max(dp[cur], dp[pre]+1)
print(n-max(dp))