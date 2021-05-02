import sys
n = int(sys.stdin.readline())
board = [sys.stdin.readline().rstrip() for _ in range(n)]
visited = [[False]*n for _ in range(n)]

cnt = 0
house_num_arr = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y):
    global cnt
    cnt+=1
    visited[x][y] = True
    for d in range(4):
        xx = dx[d] + x
        yy = dy[d] + y
        if xx >=0 and xx <n and yy>=0 and yy<n:
            if not visited[xx][yy] and board[xx][yy] != '0':
                dfs(xx,yy)

for x in range(n):
    for y in range(n):
        if not visited[x][y] and board[x][y] != '0':
            cnt = 0
            dfs(x,y)
            house_num_arr.append(cnt)
print(len(house_num_arr))
for h in sorted(house_num_arr):
    print(h)