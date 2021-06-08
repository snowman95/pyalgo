import sys, heapq
INF = int(1e9)
m,n = map(int,sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for _ in range(n)]
dx=(0,0,1,-1)
dy=(1,-1,0,0)
wall_break_cnt = [[INF]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
visited[0][0]=True
q = []
heapq.heappush(q, (0,0,0)) # 벽뚫, x,y 순서
while q:
    wb,x,y = heapq.heappop(q)
    for i in range(4):
        xx = dx[i]+x
        yy = dy[i]+y
        if xx>=0 and yy>=0 and xx<n and yy<m and not visited[xx][yy]:
            visited[xx][yy] = True
            cur_wb = wb
            if board[xx][yy] == '1': # 벽을 만남
                cur_wb +=1
            if wall_break_cnt[xx][yy] > cur_wb:
                wall_break_cnt[xx][yy] = cur_wb
                heapq.heappush(q, (cur_wb,xx,yy))
if n==1 and m==1:
    wall_break_cnt[n-1][m-1]=0
print(wall_break_cnt[n-1][m-1])