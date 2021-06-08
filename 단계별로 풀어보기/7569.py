import sys
import collections
m,n,h = map(int, sys.stdin.readline().split())
board = [[] for _ in range(h)]
normal_tomato_cnt = False
max_day = 0
q = collections.deque()
dx = (1,-1,0,0,0,0)
dy = (0,0,-1,1,0,0)
dz = (0,0,0,0,1,-1)
for z in range(h):
    for y in range(n):
        r = list(map(int, sys.stdin.readline().split()))
        normal_tomato_cnt+=r.count(0)
        board[z].append(r)
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

if normal_tomato_cnt == 0:
    print(0)
else:
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if board[z][x][y] == 1:
                    q.append((x,y,z,0))
                    visited[z][x][y] = True
    while q:
        cur = q.popleft()
        for i in range(6):
            xx = dx[i]+cur[0]
            yy = dy[i]+cur[1]
            zz = dz[i]+cur[2]
            max_day = max(max_day, cur[3])
            if xx >=0 and yy>=0 and zz>=0 and xx<n and yy<m and zz<h:
                next_day = cur[3]+1
                if not visited[zz][xx][yy] and board[zz][xx][yy] == 0:
                    normal_tomato_cnt -= 1
                    visited[zz][xx][yy] = next_day
                    q.append((xx,yy,zz,next_day))
    if normal_tomato_cnt != 0:
        print(-1)
    else:
        print(max_day)