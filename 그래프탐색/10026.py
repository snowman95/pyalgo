import sys, collections

n = int(sys.stdin.readline())
str_board = [sys.stdin.readline().rstrip() for _ in range(n)]
dx = (0,0,-1,1)
dy = (1,-1,0,0)

board = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if str_board[i][j] == 'R': board[i][j] = 0
        elif str_board[i][j] == 'G': board[i][j] = 1
        elif str_board[i][j] == 'B': board[i][j] = 2

def change_color(x,y,blind):
    global board
    if not blind:
        if board[x][y] == 2: board[x][y]=10
        else : board[x][y] = 11
    else: board[x][y] = 100

def bfs(sx,sy,blind):
    global board
    q = collections.deque([(sx,sy)])
    color = board[sx][sy]
    change_color(sx,sy,blind)
    while q:
        x,y = q.popleft()
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            if xx>=0 and yy>=0 and xx<n and yy<n:
                if not blind:
                    if board[xx][yy] < 10 and board[xx][yy] == color:
                        q.append((xx,yy))
                        change_color(xx,yy,blind)
                else:
                    if board[xx][yy] < 100 and board[xx][yy] == color:
                        q.append((xx,yy))      
                        change_color(xx,yy,blind)

not_blind_zone_cnt = 0
blind_zone_cnt = 0

for i in range(n):
    for j in range(n):
        if board[i][j] < 10:
            bfs(i,j,False)
            not_blind_zone_cnt +=1

for i in range(n):
    for j in range(n):
        if board[i][j] < 100:
            bfs(i,j,True)
            blind_zone_cnt +=1
print(not_blind_zone_cnt, blind_zone_cnt)