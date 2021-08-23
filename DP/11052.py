'''
카드 구매하기

1~N개가 포함된 카드팩 N개
- i개 카드팩 가격 = Pi
- 돈을 최대한써서 카드 N개 구매

비싼걸 최대한 취한다?? 근데 카드 N개를 맞출 수 없음.
카드 N개를 맞추면 최대한의 가격을 보장못함. 즉, 그리디 문제는 아님.

P1 = 1, P2 = 5, P3 = 6, P4 = 7
카드 4개 가지려면 P2+P2
1+1+1+1=4
1+1+5=7
5+5=10
7

P1 = 5, P2 = 2, P3 = 8, P4 = 10
카드 4개 가지려면 P3+P1

제일처음에는
dp[n] = p[n] 이렇겠고
      1     2  3  4
dp[1] 1
dp[2] 5 1+1=2
dp[3] 6 1+dp[2]
dp[4] 7 1+dp[3]

'''
import sys
n = int(sys.stdin.readline())
p = [0]+list(map(int, sys.stdin.readline().split()))
dp = p
for cnt in range(1,n+1):
    for target in range(cnt,n+1):
        dp[target] = max(dp[target], p[cnt]+dp[target-cnt])
print(dp[n])