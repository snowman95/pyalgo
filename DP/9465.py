import sys

T = int(sys.stdin.readline())
for t in range(T):
    n = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    max_score = 0

    if n == 1:
        max_score = max(arr[0][0], arr[1][0])
    else:
        dp = [[0]*n for _ in range(2)]
        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]
        dp[0][1] = arr[1][0] + arr[0][1]
        dp[1][1] = arr[0][0] + arr[1][1]

        if n == 2:
            max_score = max(max_score, max(dp[0][1],dp[1][1]))

        for i in range(2,n):
            dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + arr[0][i]
            dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + arr[1][i]
            max_score = max(max_score, max(dp[0][i],dp[1][i]))
    print(max_score)