import sys, collections
n,m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx = (0,0,1,-1)
dy = (1,-1,0,0)
empty_space_arr = []
empty_space_cnt = 0
max_safe_cnt = 0
virus_arr = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            empty_space_arr.append((i,j))
            empty_space_cnt+=1
        elif board[i][j] == 2:
            virus_arr.append((i,j))

def bfs(wall_arr):
    global board, max_safe_cnt
    q = collections.deque(virus_arr)
    visited = [[False]*m for _ in range(n)]
    for w in wall_arr:
        visited[empty_space_arr[w][0]][empty_space_arr[w][1]] = True
    while q:
        x,y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            xx = dx[i]+x
            yy = dy[i]+y
            if xx >=0 and yy>=0 and xx<n and yy<m and board[xx][yy]==0 and not visited[xx][yy]:
                q.append((xx,yy))

    safe_cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0 and not visited[i][j]:
                safe_cnt +=1
    max_safe_cnt = max(max_safe_cnt, safe_cnt)
    return
def selection(cur, wall_arr, wall_cnt):
    if wall_cnt == 3:
        bfs(wall_arr)
        return
    if cur == empty_space_cnt:
        return
    wall_arr.append(cur)
    selection(cur+1, wall_arr, wall_cnt+1)
    wall_arr.pop()
    selection(cur+1, wall_arr, wall_cnt)

selection(0,[],0)
print(max_safe_cnt)