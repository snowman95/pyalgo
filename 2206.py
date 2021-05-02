import sys
import collections
n,m= map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for _ in range(n)]
move_arr = [[[int(1e9)]*m for _ in range(n)] for _ in range(2)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
min_day = 999999

q = collections.deque([(0,0,1,False)])
move_arr[0][0][0] = 1
move_arr[1][0][0] = 1

while q:
    cur = q.popleft()
    if cur[0]==n-1 and cur[1]==m-1:
        min_day = min(min_day, cur[2])
    for i in range(4):
        xx = dx[i]+cur[0]
        yy = dy[i]+cur[1]
        if xx >=0 and yy>=0 and xx<n and yy<m:
            next_day = cur[2]+1
            broken = cur[3]
            if  board[xx][yy] == '0':
                if move_arr[broken][xx][yy] > next_day:
                    move_arr[broken][xx][yy] = next_day
                    q.append((xx,yy,next_day,broken))
            else:
                if broken == False and move_arr[1][xx][yy] > next_day:
                    move_arr[1][xx][yy] = next_day
                    q.append((xx,yy,next_day, True))

if min_day == 999999:
    print(-1)
else:
    print(min_day)