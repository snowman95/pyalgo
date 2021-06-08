import sys
dx = (1,-1,0,0,-1,-1,1,1)
dy = (0,0,1,-1,-1,1,-1,1)

def dfs(x,y):
    global visited, xx, yy
    visited[x][y] = True
    for i in range(8):
        xx = dx[i]+x
        yy = dy[i]+y
        if xx>=0 and yy>=0 and xx<n and yy<m:
            if board[xx][yy] == 1 and not visited[xx][yy]:
                dfs(xx,yy)
while True :
    m,n = map(int,sys.stdin.readline().split())
    if m==0 and n==0:
        break
    board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and not visited[i][j] :
                dfs(i,j)
                cnt+=1

    print(cnt)