'''
이동하기

NxM 미로
좌측상단이 (1,1), 우측하단이 (N,M)
준규는 (1,1)→(N,M)

아래 1칸, 오른 1칸, 우측하단 대각선으로 1칸
이렇게 3가지 이동 가능함

dp[n][m] = max(dp[n-1][m], dp[n][m-1], dp[n-1][m-1])
'''
import sys, collections
n, m = map(int, sys.stdin.readline().split())
candy = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0][0] = candy[0][0]
dx = (0,1,1)
dy = (1,0,1)
q = collections.deque([(0,0,candy[0][0])])
visited = [[False]*m for _ in range(n)]
visited[0][0] = True
total_candy = 0
while q:
    x,y,c = q.popleft()
    if x == n-1 and y == m-1:
        total_candy = max(total_candy, dp[n-1][m-1])
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            if nx == 0:
                dp[nx][ny] = dp[0][ny-1] + candy[0][ny]
            elif ny == 0:
                dp[nx][ny] = dp[nx-1][0] + candy[nx][0]
            else:
                dp[nx][ny] = max(dp[nx][ny-1], dp[nx-1][ny], dp[nx-1][ny-1]) + candy[nx][ny]
            q.append((nx,ny,dp[nx][ny]))

print(total_candy)