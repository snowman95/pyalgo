'''
맥주 마시면서 걸어가기

직사각형 맵
맥주 1box = 맥주20개
맥주 1병 = 50m 이동, 1box = 1000m
편의점 들렸을 때 빈 병을 새 맥주로 교환 가능

테케(t<=50)
맥주파는 편의점 n(0~100)
집, 편의점, 페스티벌 좌표 (x,y -32768~32768)
거리차이 = abs(x1-x2)+abs(y1-y2)

각 좌표간 거리를 계산해서 그래프를 만들어야함.
집 = 0
편의점 = 1~n
페스티벌 = n+1

집-편의점-페스티벌은 모두 이어져 있다고 가정하고
인접 행렬에다가 이중 for문으로 모든 경로비용 계산.
만약에 경로가 1000넘어가면 INF
'''
import sys
T = int(sys.stdin.readline())
for t in range(T):
    n = int(sys.stdin.readline())
    INF = (n+2)*32767+1
    arr = [[INF]*(n+2) for _ in range(n+2)]
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n+2)]
    for i in range(n+2):
        arr[i][i] = 0
        x,y = board[i]
        for j in range(n+2):
            if i == j : continue
            nx,ny = board[j]
            dist = abs(x-nx)+abs(y-ny)
            if dist <= 1000:
                arr[i][j] = dist

    for k in range(n+2):
        for i in range(n+2):
            for j in range(n+2):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

    if arr[0][n+1] != INF:
        print('happy')
    else:
        print('sad')