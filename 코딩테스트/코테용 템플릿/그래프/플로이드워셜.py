'''
플로이드 워셜

V(노드) 개수가 200개 이하이고, 모든노드에서 모든노드로 가는 경우 알아야 할때

i → k (임의의 위치)를 찍고
k → a (a로)
k → b (b로)
k → c (b로)
이렇게 가는 경우의 최소비용 구하는 방법
for i in range(k):
    result = min(result, arr[i][k]+arr[k][a]+arr[k][b]+arr[k][c])

'''

import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = n*m+1
arr = [[INF]*n for _ in range(n)]
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    arr[a-1][b-1] = 1

for i in range(n):
    arr[i-1][i-1] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

for i in range(n):
    cnt = 0
    for j in range(n):
        if arr[i][j] == INF and arr[j][i] == INF:
            cnt +=1
    print(cnt)


'''
사이클 확인

자기자신으로 가는것을 0으로 초기화 하지말고 INF 그대로 둠
결과에 INF가 아닌 다른값이 들어있다면 나 자신으로 돌아왔다 (사이클 형성했다)
사이클을 형성하는 경우 arr[i][j] + arr[j][i] 의 최소값이 최소 사이클 비용이다.
'''
import sys
n, e = map(int, sys.stdin.readline().split())
INF = n*e+1
arr = [[INF]*n for _ in range(n)]
for i in range(e):
    a,b,c = map(int, sys.stdin.readline().split())
    arr[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

min_cycle_dist = INF
for i in range(n):
    if arr[i][i] != INF:
        for j in range(n):
            min_cycle_dist = min(min_cycle_dist, arr[i][j]+arr[j][i])
if min_cycle_dist == INF:
    min_cycle_dist = -1
print(min_cycle_dist)