'''
이전
'''

import sys
n = int(sys.stdin.readline())
price = [0]
price += [int(sys.stdin.readline()) for _ in range(n)]
dp = [0] * (n+1)
dp[1] = price[1]

if n>1:
    dp[2] = price[1]+price[2]

for i in range(3,n+1):
    dp[i]=max(dp[i-1], dp[i-3]+price[i-1]+price[i], dp[i-2]+price[i])

print(dp[n])