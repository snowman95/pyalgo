'''
미로만들기

nxn 바둑판 모양 (1~50)
0 : 검은방 - 못감
1 : 흰방   - 갈 수 있음

시작과 끝은 항상 흰방.
시작 → 끝으로 못가는 경우가 있을 수 있음.
검은방 몇개를 흰방으로 바꿀것.

하나도 안바꿔도 된다면 0 출력
바꿔야하면 최소로 바꿔야할 개수 출력

[아이디어]
막다른길 만나면 벽 뚫는다.
visited 배열에 방문여부와 내가 벽뚫은 횟수를 같이 기록함.
전체를 -1로 초기화 했기 때문에 방문할 때마다 검사/초기화
방문위치가 -1 이거나 현재위치의 wall_break보다 적어야 진행가능

dfs vs bfs : 모두 동일한 level로 진행필요하므로 bfs 선택
'''
import sys,collections
n = int(sys.stdin.readline())
board = list(sys.stdin.readline().strip() for _ in range(n))
dx = (0,0,1,-1)
dy = (1,-1,0,0)

min_wall_break_cnt = sys.maxsize
wall_break = [[-1]*n for _ in range(n)]
q = collections.deque([(0,0,0)])
wall_break[0][0]=0

while q:
    x,y,wall = q.popleft()
    if x == n-1 and y == n-1:
        min_wall_break_cnt = min(min_wall_break_cnt, wall)
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if 0<=nx<n and 0<=ny<n:
            if wall_break[nx][ny] == -1 or wall < wall_break[nx][ny]:
                if board[nx][ny] == '1':
                    wall_break[nx][ny] = wall
                    q.append((nx,ny,wall))
                else:
                    wall_break[nx][ny] = wall+1
                    q.append((nx,ny,wall+1))

if min_wall_break_cnt == sys.maxsize:
    min_wall_break_cnt = 0
print(min_wall_break_cnt)