'''
1,2,3 더하기

정수 n을 1,2,3의 합으로 나타낼 수 있는 방법의 수

4 를 1,2,3의 합으로 나타내는 방법
1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1

[아이디어]
dp[n] = ?

1 = 1

2 = 1+1 (1과 동일)
  = 2
  = 1 + dp[1] + dp[1] -1 = 2

3 = dp[2] = 1+1+1, 1+2, 2+1
  = dp[1] = 2+1
  = 4

4 = dp[3] = 1+1+1+1, 1+1+2, 1+2+1, 1+3
    dp[2] = 2+1+1, 2+2
    dp[1] = 3+1
  = 7

5 = dp[4] = 1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+1+3, 1+2+1+1, 1+2+2, 1+3+1,
    dp[3] = 2+1+1+1, 2+1+2, 2+2+1 2+3
    dp[2] = 3+1+1, 3+2
    = 2+4+7=13

6 = dp[5]+dp[4]+dp[3] = 4+7+13 = 24
7 = 7+13+24 = 44
'''
import sys
T = int(sys.stdin.readline())
dp = [1,2,4] + [0]*9
for i in range(3,12):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

for t in range(T):
    n = int(sys.stdin.readline())
    print(dp[n-1])