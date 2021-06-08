import sys
import operator
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp1 = [1]*n
dp2 = [1]*n


for cur in range(1, n):
    for front in range(0, cur):
        if arr[front] < arr[cur]:
            dp1[cur] = max(dp1[cur], dp1[front]+1)
for cur in range(n-2, -1, -1):
    for rear in range(cur+1, n):
        if arr[cur] > arr[rear]  :
            dp2[cur] = max(dp2[cur], dp2[rear]+1)

dp1_max_value = max(dp1)
dp2_max_value = max(dp2)
dp1_cadi = 0
dp2_cadi = 0

dp1_max_index = list(filter(lambda x: dp1[x] == dp1_max_value, range(n)))
dp2_max_index = list(filter(lambda x: dp2[x] == dp2_max_value, range(n)))
'''
for i in dp1_max_index:
    if i == n-1: dp1_cadi = max(dp1_cadi, dp1[i])
    else: dp1_cadi = max(dp1_cadi, dp1[i] + dp2[i+1])

for i in dp2_max_index:
    if i == 0: dp2_cadi = max(dp2_cadi, dp2[i])
    else: dp2_cadi = max(dp2_cadi, dp2[i] + dp1[i-1])

print(max(dp1_cadi,dp2_cadi))

'''