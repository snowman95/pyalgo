'''
가장 큰 증가 부분 수열

LIS 중에 합이 젤 큰것을 고르면 된다.

dp[n] = 현재 인덱스까지의 최대 합
'''
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = arr.copy()
for cur in range(1, n): 
    for front in range(cur): 
        if arr[front] < arr[cur]:
            dp[cur] = max(dp[cur], dp[front]+arr[cur])
print(max(dp))