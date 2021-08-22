'''
돌 게임2
돌 N개 
상근/창역이가 번갈아가며 돌 1개 또는 3개 가져간다.
마지막에 돌 가져가면 진다. 이기는 사람 구해라

아이디어
N=4
1 1 1 1
1 3

dp[n] = n번 째에 돌을 가져가는 사람?

첫턴에 1 또는 3임

'''
import sys
n = int(sys.stdin.readline())
dp = ['0'] * (n+4)
for i in range(1,n+1):
    if i%2:
        dp[i] = "SK"
        dp[i+3] = "SK"
    else :
        dp[i] = "CY"
        dp[i+3] = "CY"

if dp[n] == "CY":
    print("SK")
else:
    print("CY")