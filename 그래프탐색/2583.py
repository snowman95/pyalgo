import sys
sys.setrecursionlimit(50000)
dx = (1,-1,0,0)
dy = (0,0,1,-1)

def dfs(x,y,cnt):
    global visited, xx, yy, board_range
    board[x][y] = True
    board_range +=1
    for i in range(4):
        xx = dx[i]+x
        yy = dy[i]+y
        if xx>=0 and yy>=0 and xx<n and yy<m:
            if board[xx][yy] == False:
                dfs(xx,yy,cnt+1)

n,m,k = map(int,sys.stdin.readline().split())
board = [[False] * m for _ in range(n)]
for _ in range(k):
    a,b,c,d = map(int,sys.stdin.readline().split())
    x1 = n-b-1
    y1 = a
    x2 = n-d
    y2 = c-1
    for x in range(x2,x1+1):
        for y in range(y1,y2+1):
            board[x][y] = True

ans = []
for i in range(n):
    for j in range(m):
        if board[i][j] == False:
            board_range = 0
            dfs(i,j,1)
            ans.append(board_range)
print(len(ans))
ans.sort()
for a in ans:
    sys.stdout.write(str(a)+' ')