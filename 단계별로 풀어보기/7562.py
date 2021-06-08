import sys
import collections

dx = (-1,-2,-2,-1,1,2,2,1)
dy = (-2,-1,1,2,2,1,-1,-2)
T = int(sys.stdin.readline())

for i in range(T):
    board_size = int(sys.stdin.readline())
    sx,sy = map(int, sys.stdin.readline().split())
    ex,ey = map(int, sys.stdin.readline().split())

    visited = [[False]*board_size for _ in range(board_size)]
    visited[sx][sy] = True
    q = collections.deque([(sx,sy,0)])
    
    while q:
        cur = q.popleft()
        if cur[0]==ex and cur[1]==ey:
            print(cur[2])
            break
        for i in range(8):
            xx = dx[i]+cur[0]
            yy = dy[i]+cur[1]
            if xx >=0 and yy>=0 and xx<board_size and yy<board_size:
                next_move = cur[2]+1
                if not visited[xx][yy]:
                    q.append((xx,yy,next_move))
                    visited[xx][yy] = True