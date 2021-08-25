'''
파이프 옮기기 1

NxN 격자판. 각 칸은 (r,c)
(1,1),(1,2) 위치 파이프 → (N,N)까지 이동

빈칸 0
벽 1

파이프는 3가지 방향가능
1. 가로 (x,y+1)
2. 세로 (x+1,y)
3. 대각선 (x,y+1), (x+1,y+1), (x+1,y) 
  - 가로일땐 아래 1칸으로 꺾기 (x,y+1), (x+1,y+1), (x+1,y) 
  - 세로일땐 우측 1칸으로 꺽기 (x+1,y), (x+1,y+1), (x,y+1)

※ 대각선을 이동 못하는 경우를 잘 고려하여 로직 짜야함


[초기화]
(1,1),(1,2) 위치에 파이프
board[1][1] = 1
board[1][2] = 1
visited[1][1] = True
visited[1][2] = True


[로직]
bfs 수행하여 N,N 도달할 때까지 진행.
1. 파이프 옮길 수 있는지 Check
2. 놓을 수 있는 모든 방법의 파이프
3. (N,N) 도달 시 cnt+=1

'''
import sys
n = int(sys.stdin.readline())
board = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
board[0][0]=1
board[0][1]=1
cnt = 0
# 가로(0), 세로(1), 대각(2)
def dfs(x,y,dir):
    global board, cnt
    if x==n-1 and y==n-1:
        cnt+=1
        return
    board[0][1]=2
    if 0<=x+1<n and 0<=y+1<n and board[x+1][y+1]==board[x+1][y]==board[x][y+1]==0:
        dfs(x+1,y+1,2)
    if (dir==0 or dir==2) and 0<=x<n and 0<=y+1<n and board[x][y+1]==0:
        dfs(x,y+1,0)
    if dir>=1 and 0<=x+1<n and 0<=y<n and board[x+1][y]==0:
        dfs(x+1,y,1)
    board[0][1]=0
if board[n-1][n-1] != 1: dfs(0,1,0)
print(cnt)