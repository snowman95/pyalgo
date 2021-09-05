'''
경로 찾기

가중치 없는 그래프
모든 정점에서 다른 정점가는 경로 있는지 확인

정점 수 N (1~N)
i j 0 : 경로없음
i j 1 : 경로있음

'''
import sys
n = int(sys.stdin.readline())
INF = n * 1 + 1
arr = [[INF] * n for _ in range(n)]

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if row[j] == 1:
            arr[i][j] = row[j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

for i in range(n):
    for j in range(n):
        if arr[i][j] == INF: arr[i][j] = 0
        if arr[i][j] >= 1: arr[i][j] = 1
    print(*arr[i])