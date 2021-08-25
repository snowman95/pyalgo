'''
돌 게임

탁자 위 N개의 돌
상근/창역 번갈아가며 1개or3개 돌 가져감
마지막에 돌 가져가는 사람이 이김

상근이가 먼저 겜 시작. 이기는 사람은??
'''
import sys
n=int(sys.stdin.readline())
dp = ['0','SK']*(n+1)
if n == 1:
    print("SK")
    sys.exit()
for i in range(1,n+1):
    if dp[i-1] == "SK":
        dp[i] = "CY"
        dp[i+3] = "CY"
    else:
        dp[i] = "SK"
        dp[i+3] = "SK"
print(dp[n])