import sys
sys.setrecursionlimit(15000)
n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
min_h,max_h = 101,0
max_safe_zone_cnt = 1
for i in range(n):
    for j in range(n):
        min_h = min(min_h, board[i][j])
        max_h = max(max_h, board[i][j])

dx = (0,0,1,-1)
dy = (1,-1,0,0)

def dfs(x,y,h):
    global board, visited
    visited[x][y] = True

    for i in range(4):
        xx = dx[i] + x
        yy = dy[i] + y
        if xx >=0 and yy>=0 and xx <n and yy<n and not visited[xx][yy] and board[xx][yy] > h:
            dfs(xx,yy,h)

for h in range(min_h,max_h):
    cnt = 0
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > h and not visited[i][j]:
                cnt +=1
                dfs(i,j,h)
    max_safe_zone_cnt = max(max_safe_zone_cnt, cnt)
print(max_safe_zone_cnt)