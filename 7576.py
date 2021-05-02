import sys
import collections
m,n = map(int, sys.stdin.readline().split())
board = []
normal_tomato_cnt = False
max_day = 0
dx = [1,-1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    r = list(map(int, sys.stdin.readline().split()))
    normal_tomato_cnt+=r.count(0)
    board.append(r)
visited = [[False]*m for _ in range(n)]
q = collections.deque()

if normal_tomato_cnt == 0:
    print(0)
else:
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                q.append((i,j,0))
                visited[i][j] = True
    while q:
        cur = q.popleft()
        for i in range(4):
            xx = dx[i]+cur[0]
            yy = dy[i]+cur[1]
            max_day = max(max_day, cur[2])
            if xx >=0 and yy>=0 and xx<n and yy<m:
                next_day = cur[2]+1
                if not visited[xx][yy] and board[xx][yy] == 0:
                    normal_tomato_cnt -= 1
                    visited[xx][yy] = next_day
                    q.append((xx,yy,next_day))
    if normal_tomato_cnt != 0:
        print(-1)
    else:
        print(max_day)