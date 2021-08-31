'''
숫자판 점프

5x5 숫자판
각 칸에 숫자 0~9가 적혀있다.
start = 임의 위치 

인접 4방향으로 총 5번 이동하여
각 칸의 숫자 차례로 붙이면 6자리 수됨
왔던곳 다시 가도 되고, 0으로 시작해도 노상관

서로 다른 6자리의 수의 개수 구하라

[아이디어]
1. 일단 왔던곳을 다시 갈 수 있음.
2. 무조건 5번동안 이동만 하면 됨.

'''
import sys,collections
board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
dx = (0,0,1,-1)
dy = (1,-1,0,0)
total = set()
def bfs(sx,sy):
    global board
    arr = [board[sx][sy]]
    q = collections.deque([(sx,sy,arr)])
    while q:
        x,y,arr = q.popleft()
        if len(arr) == 6:
            total.add(''.join(map(str, arr)))
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<5 and 0<=ny<5 :
                q.append((nx,ny,arr+[board[nx][ny]]))

for x in range(5):
    for y in range(5):
        bfs(x,y)
print(len(total))