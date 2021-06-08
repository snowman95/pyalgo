import sys
T = int(sys.stdin.readline())
board = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
   board[x][y] = False
   for d in range(4):
       xx = dx[d] + x
       yy = dy[d] + y
       if xx >=0 and xx <n and yy>=0 and yy<m:
           if board[xx][yy]:
               dfs(xx,yy)

for t in range(T):
    n,m,k = map(int, sys.stdin.readline().split())

    board = [[False]*m for _ in range(n)]
    for i in range(k):
        x,y= map(int, sys.stdin.readline().split())
        board[x][y] = True

    cnt = 0
    for x in range(n):
        for y in range(m):
            if board[x][y]:
                cnt +=1
                dfs(x,y)
    print(cnt)