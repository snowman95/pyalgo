2189.pyimport sys
board = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m,k = map(int, sys.stdin.readline().split())
board = [[False]*m for _ in range(n)]
for i in range(k):
    x,y= map(int, sys.stdin.readline().split())
    board[x][y] = True

def dfs(x,y):
       board[x][y] = False
   for d in range(4):
       xx = dx[d] + x
       yy = dy[d] + y
       if xx >=0 and xx <n and yy>=0 and yy<m:
           if board[xx][yy]:
               dfs(xx,yy)

cnt = 0
for x in range(n):
    for y in range(m):
        if board[x][y]:
            cnt +=1
            dfs(x,y)
print(cnt)