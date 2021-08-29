'''
동전

테스트케이스 T개 (1~10)
  동전 종류 N개 (1~20)
  N가지 동전의 금액이 오름차순으로 주어짐 (1~10000원)
  N가지 동전으로 만들 금액 (1~10000원)

[아이디어]
3

2
1 2
1000 = 1과 2로만 만들어야함

3
1 5 10
100 = 1과 5와 10로만 만들어야함

2
5 7
22 = 5와 7로만 만들어야함

그리드 vs dp = dp
그리드는 동전 금액이 전부 배수 관계 있어야 함. 고로 dp문제다.

dp[n] = 금액n을 만들 수 있는 모든 횟수

코인 가격 5라고치면
5부터 22까지 쭉 증가시키면서
dp[5] += dp[5-5]
dp[6] += dp[6-5]


'''
import sys
T = int(sys.stdin.readline())
for t in range(T):
    n = int(sys.stdin.readline())
    coin = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())
    dp = [0] * 10001
    for c in coin:
        dp[c]+=1
        for j in range(c,target+1):
            dp[j] += dp[j-c]
    print(dp[target])