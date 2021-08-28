'''
양

직사각형의 우리
. 빈자리
# 울타리
o 양
v 늑대

양과 늑대 싸운다.
양의 수 <= 늑대의 수 : 늑대가 양 먹음
양의 수 > 늑대의 수 : 양 늑대 먹음


[아이디어]
처음에 양의 수, 늑대의 수 count

dfs 돌면서
양의 수, 늑대 수 count 해서 위와 같은 조건에 따라 제거

'''
import sys, collections
r, c = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(r)]
sheep = 0
wolf = 0
empty_space = []
visited = [[False]*c for _ in range(r)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(r):
    for j in range(c):
        if board[i][j] == "v":
            wolf+=1
        elif board[i][j] == "o":
            sheep+=1
        if board[i][j] != "#":
            empty_space.append((i,j))

def dfs(sx,sy):
    global r,c,visited,board
    q = collections.deque([(sx,sy)])
    sheep=0
    wolf=0
    visited[sx][sy] = True

    while q:
        x,y = q.popleft()
        if board[x][y]=="v":    wolf+=1
        elif board[x][y] =="o": sheep+=1
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and board[nx][ny]!="#":
                visited[nx][ny] = True
                q.append((nx,ny))
    return (sheep, wolf)

for x,y in empty_space:
    if not visited[x][y]:
        s, w = dfs(x,y)
        if s <= w: sheep -= s
        else: wolf -= w
print(sheep, wolf)