'''
저울

무게 서로다른 물건 N개 (1~N 번호) (5~100)
무거움 측정표 가지고 
물건 N개와 일부 물건 상의 비교결과 M개 (0~2000)
다른 모든 물건과 비교결과 알 수 있는것 개수 count

물건 = 노드
무게비교결과 = 간선비용
[a][b] = INF (알 수 없음)
[a][b] = 1 (a가 b보다 무거움)
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