import sys,collections
n,l,r = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx = (1,-1,0,0)
dy = (0,0,1,-1)

def bfs(sx,sy, union, union_num):
    global board
    q = collections.deque([(sx,sy)])
    unions = [(sx,sy)]
    union[sx][sy] = union_num
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and union[nx][ny] == 0:
                if l<=abs(board[x][y]-board[nx][ny])<=r:
                    q.append((nx,ny))
                    unions.append((nx,ny))
                    union[nx][ny] = union_num
                    cnt+=1
    total_people = 0
    for x,y in unions:
        total_people += board[x][y]
    total_people//=cnt
    for x,y in unions:
        board[x][y] = total_people
    return cnt
        
people_move_cnt = 0
while True:
    union = [[0]*n for _ in range(n)]
    union_num = 1
    for i in range(n):
        for j in range(n):
            if union[i][j] == 0:
                cnt = bfs(i,j,union,union_num)
                if cnt != 1 : 
                    union_num+=1
    if union_num == 1:
        break
    people_move_cnt+=1
print(people_move_cnt)