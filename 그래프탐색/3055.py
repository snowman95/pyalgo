import sys, collections
r,c = list(map(int,sys.stdin.readline().split()))
input_board = [sys.stdin.readline().rstrip() for _ in range(r)]
board = [[[] for _ in range(c)] for _ in range(r)]

visited = [[False]*c for _ in range(r)]
dx=(1,-1,0,0)
dy=(0,0,1,-1)
water_q = collections.deque()
sonic_q = collections.deque()
time = 0
is_finished = False
for i in range(r):
    for j in range(c):
        if input_board[i][j] == 'S':
            board[i][j] = 0
            sonic_q.append((i,j))
            visited[i][j] = True
        elif input_board[i][j] == '*':
            water_q.append((i,j))
            board[i][j] = 1
        elif input_board[i][j] == 'X':
            board[i][j] = 2
        elif input_board[i][j] == 'D':
            board[i][j] = 3
        else:
            board[i][j] = 0

def bfs(q, sonic):
    global board,visited, is_finished
    new_q = collections.deque()
    while q:
        x,y = q.popleft()
        if sonic and board[x][y] == 3:
            is_finished = True
            return new_q
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<r and 0<=ny<c :
                if sonic :
                    if not visited[nx][ny]:
                       if board[nx][ny]==0 or board[nx][ny]==3:
                            visited[nx][ny]= True
                            new_q.append((nx,ny))
                else:
                    if board[nx][ny]==0:
                        board[nx][ny] = 1
                        new_q.append((nx,ny))
    return new_q


# 물을 먼저 퍼뜨리고, 고슴도치 출발
while True:
    water_q = bfs(water_q, False)
    sonic_q = bfs(sonic_q, True)
    if is_finished:
        break
    # 근데 물이 더 퍼지지 못하고, 고슴도치도 움직이지 못하는 경우?
    if not water_q and not sonic_q:
        break
    time +=1

if is_finished:
    print(time)
else:
    print("KAKTUS")