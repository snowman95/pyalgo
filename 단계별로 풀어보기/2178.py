import sys
import collections
n,m = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for i in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
#min_visit_arr = [[int(1e9)]*m for _ in range(n)]
def bfs(x,y, visited):
    q = collections.deque([(x,y,1)])
    visited[x][y] = True
    while q:
        cur = q.popleft()
        if cur[0]==n-1 and cur[1] ==m-1 :
            print(cur[2])
            return
        for i in range(4):
            xx = dx[i] + cur[0]
            yy = dy[i] + cur[1]
            if xx >=0 and yy>=0 and xx<n and yy<m :
                if not visited[xx][yy] and board[xx][yy] == '1':
                    visited[xx][yy] = True
                    q.append((xx,yy,cur[2]+1))
bfs(0,0, [[False]*m for _ in range(n)])