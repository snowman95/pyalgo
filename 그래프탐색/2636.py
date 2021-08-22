'''
치즈

nxn 정사각형 판 (최대 100x100)
0은 치즈 없는 칸
1은 치즈 있는 칸 - 하나이상 구멍 존재
0으로 둘러싸인

첫째 줄에는 치즈가 모두 녹아서 없어지는 데 걸리는 시간을 출력하고, 
둘째 줄에는 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 출력한다.

연결이 안된 치즈들이 각각의 섬이라 생각하고
각 섬의 가장자리가 1시간마다 녹는다.

[초기화]
이중 for문으로 cheeze_cnt 카운팅
time = 0

[반복]
1. 벽의 가장자리에서 bfs 탐색으로 갈 수 있는 모든 0을 queue에 담는다.
2. old_cheeze_cnt=0,  bfs 탐색. 
  - visted=False만 진행가능.
  - 0만나면 visited=true
  - 1만나면 (값=0, visited=true), old_cheeze_cnt+1, new_air_queue 에 넣기
  - bfs 한턴 다 끝나면 time+1, cheeze_cnt-old_cheeze_cnt.
  - 이때 만약 cheeze_cnt=0 되면 old_cheeze_cnt 반환
3. new_air_queue에 넣은걸로 다시 bfs 탐색 할건데
  - visited
'''
import sys
x,y = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(x)]
dx = (1,0,0,-1)
dy = (0,1,-1,0)

time = 0
cheeze_cnt = 0
air_queue = []
visited = [[False] *y for _ in range(x)]
for row in arr:
    cheeze_cnt += row.count(1)

# 가장자리 air 표시
for i in range(y):
    if arr[0][i] == 0:   air_queue.append((0,i))
    if arr[x-1][i] == 0: air_queue.append((x-1,i))
for j in range(1,x-1):
    if arr[j][0] == 0:   air_queue.append((j,0))
    if arr[j][y-1] == 0: air_queue.append((j,y-1))
for i,j in air_queue:
    visited[i][j] = True

def bfs(q):
    global x,y,visited
    new_air_queue = []
    while q:
        i,j = q.pop()
        for d in range(4):
            nexti = dx[d] + i
            nextj = dy[d] + j
            if 0<nexti<x and 0<nextj<y and not visited[nexti][nextj]:
                visited[nexti][nextj]=True
                if arr[nexti][nextj] == 1:
                    arr[nexti][nextj] = 0
                    new_air_queue.append((nexti,nextj))
                else:
                    q.append((nexti,nextj))
    return new_air_queue

if cheeze_cnt == 0:
    print(0)
    print(0)

while cheeze_cnt:
    air_queue = bfs(air_queue)
    old_cheeze_cnt = len(air_queue)
    if cheeze_cnt-old_cheeze_cnt == 0:
        print(time+1)
        print(cheeze_cnt)
        break
    cheeze_cnt-=old_cheeze_cnt
    time +=1