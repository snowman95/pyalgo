import sys
'''
dp[i] = i번 연산했을때 최소값 (x)
dp[i] = i라는 숫자를 만들 수 있는 최소 연산 횟수 (o)

초기값
dp[1] = 0

과정
1이라는 숫자로 *2, *3, +1을 하여 만들 수 있는
'''

dp = [int(1e9)] * 3000003
n = int(sys.stdin.readline())
dp[1] = 0

for i in range(1, n+1):
    dp[i*2] = min(dp[i*2], dp[i]+1)
    dp[i*3] = min(dp[i*3], dp[i]+1)
    dp[i+1] = min(dp[i+1], dp[i]+1)
print(dp[n])