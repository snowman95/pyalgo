'''
플로이드

정점 n(2~100)
노드 m(1~100000)

모든 도시 A->B로 가는 최소값 구해라
'''
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = n*100000+1
arr = [[INF]*n for _ in range(n)]
for i in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    arr[a-1][b-1] = min(arr[a-1][b-1], c)

for i in range(n):
    arr[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

for i in range(n):
    for j in range(n):
        if arr[i][j] == INF:
            arr[i][j] = 0

for a in arr:
    print(*a)