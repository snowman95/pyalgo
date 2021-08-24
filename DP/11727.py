'''
2xn 타일링 2

2xn 직사각형을 1x2, 2x1, 2x2로 채우기

dp[n] = n 길이의 직사각형 그리는 방법
dp[1] = 1 (세로 1개)
dp[2] = 3 (가로 2개 , 세로 2개 , 직사각형 1개)
dp[3] = 5 (dp[1] 에서 가로2개, 세로2개 + dp[2] 에서 세로 1개씩 붙임)
dp[4] = 11
'''
import sys
n = int(sys.stdin.readline())
dp = [0,1,3] + [0]*(n-2)
for i in range(3,n+1):
    dp[i] = dp[i-2]*2 + dp[i-1]
print(dp[n]%10007)