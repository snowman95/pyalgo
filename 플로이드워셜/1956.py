'''
운동

마을 V개 (2~400) - 시간제한 2초라서 O(n^3) 가능
도로 E개 (0~v(v-1))

a,b,c = a->b사이 거리가 c인 도로
거리 합이 최소가 되는 사이클을 찾아야 함

1. 사이클
사이클이란 결국 a->...->a 이렇게 되는 거잖아?
1->2->3->1
1->2->1
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