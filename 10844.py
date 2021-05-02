import sys
n = int(sys.stdin.readline())
'''
dp[i][j] = i라는 숫자로 시작하는 길이 j의 숫자 개수
'''
dp = [[0]*(n+1) for _ in range(10)]

for i in range(0,10):
    dp[i][1] = 1

for length in range(2,n+1):
    for num in range(0,10):
        if num == 0:
            dp[num][length] = dp[num+1][length-1]
        elif num == 9:
            dp[num][length] = dp[num-1][length-1]
        else:
            dp[num][length] = dp[num+1][length-1] + dp[num-1][length-1]

total = 0
for i in range(1,10):
    total += dp[i][n]
print(total%1000000000)