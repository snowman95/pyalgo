'''
DFS 풀이시 재귀 한도 풀어줘야 함.
sys.setrecursionlimit(제한횟수)


(공식) 가중치가 없는 최단 경로 : BFS
DFS : 특정 칸에 처음 도달했을 때까지의 경로 길이가 다른 경로를 통해 도달한 길이보다 짧다는 보장못함.
BFS : 특정 칸에 처음 도달했을 때까지의 경로 길이가 항상 최적임을 보장

(권장) DFS는 스텍 터질 위험이 크므로 BFS 사용
(권장) 최대 길이를 구하는 문제는 BFS 가 유리하다는 의견이 많음

'''
import sys
sys.setrecursionlimit(10000)

# DFS 기본형태
def dfs(arr, cur, visited):
    visited[cur] = True
    for i in arr[cur]:
        if not visited[i]:
            dfs(arr, cur, visited)

# BFS 기본형태
visited = [False] * 100
from collections import deque

def bfs(arr, start, visitet):
    queue = deque([start])
    visited[start] = True
    while queue:
        cur = queue.popleft()
        for i in arr[cur]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

'''
(인접행렬) 4방향 이동하여 목적지까지 도달

2차원 바둑판 형태의 입력
상하좌우 4방향으로 말을 이동하여 최단 경로로 목적지 까지 도착하는 문제
dx, dy라는 move offset 변수를 두어서, 상하좌우 이동을 for문 하나로 구현한다.
'''
import collections
n = 10
m = 10
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y, board, visited):
    # 시작점도 이동 카운트로 치면 큐에 1 넣고, 아니면 0으로
    q = collections.deque([(x,y,1)])
    visited[x][y] = True
    while q:
        cur = q.popleft()
        # 목적지 도달한 경우 (BFS는 현재가 항상 최적 경로임을 보장)
        if cur[0]==n-1 and cur[1] ==m-1 :
            print(cur[2])
            return
        for i in range(4):
            xx = dx[i] + cur[0]
            yy = dy[i] + cur[1]
            if 0<=xx<n and 0<=yy<m and not visited[xx][yy] and board[xx][yy] == '1':
                visited[xx][yy] = True
                q.append((xx,yy,cur[2]+1))

''' 
(인접행렬) 8방향 이동하여 독립된 지역 개수 확인

2차원 바둑판 형태의 입력
상하좌우대각선, 총 8방향으로 1칸이라도 붙어있으면 인접하다고 가정
(0,0)부터 (n,m)까지 이중 for문을 돌면서 방문하지 않은 곳을 시작점으로 잡고 방문가능한 곳을 모두 방문한다. 
즉, BFS/DFS를 수행하면 하나의 독립된 지역을 탐색하는 것이다. 지역+1을 해준다.
'''
board = [[]]
dx = (1,-1,0,0,-1,-1,1,1)
dy = (0,0,1,-1,-1,1,-1,1)

def dfs(x,y):
    global visited, xx, yy
    visited[x][y] = True
    for i in range(8):
        xx = dx[i]+x
        yy = dy[i]+y
        # 이 예시에서는 board가 1인 지역을 방문 가능하다고 가정
        if 0<=xx<n and 0<=yy<m and board[xx][yy] == 1 and not visited[xx][yy]:
            dfs(xx,yy)

visited = [[False] * m for _ in range(n)]
cnt = 0   # 독립된 지역의 개수
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j] :
            dfs(i,j) # 하나의 독립된 지역을 탐색
            cnt+=1


'''
(인접 행렬) 정상 노드 감염 시키기

2차원 바둑판 형태의 입력
상하좌우, 총 4방향으로 1칸이라도 붙어있으면 인접하다고 가정
정상 노드와 감염 노드가 존재함
감염된 노드는 매초마다 인접한 방향으로 퍼져나간다. 정상 노드를 만나면 감염 노드로 변이시킨다.
더 이상 감염시킬 노드 없을 때 까지 진행
감염된 노드들을 모두 큐에 넣고 시작. 전파 중에 새롭게 감염된 노드만 큐에 넣음

'''
visited = [[False]*m for _ in range(n)]
q = collections.deque()
normal_tomato_cnt = 0
for i in range(n):
        for j in range(m):
        # 이 예시에서는 board가 1인 노드가 감염 노드로 간주 = 모두 큐에 넣는다.
            if board[i][j] == 1:
                q.append((i,j,0))
                visited[i][j] = True
while q:
        cur = q.popleft()
        for i in range(4):
            xx = dx[i]+cur[0]
            yy = dy[i]+cur[1]
            max_day = max(max_day, cur[2])
            if xx >=0 and yy>=0 and xx<n and yy<m:
                next_day = cur[2]+1
                # 이 예시에서는 board가 0인 노드를 새롭게 감염시킨다고 가정
                if not visited[xx][yy] and board[xx][yy] == 0:
                    normal_tomato_cnt -= 1
                    visited[xx][yy] = next_day
                    q.append((xx,yy,next_day))


'''
(인접 행렬) 동일 위치에 재 방문이 가능한 경우

2차원 바둑판 형태의 입력
상하좌우, 총 4방향으로 1칸이라도 붙어있으면 인접하다고 가정
문제의 특수한 조건 때문에 같은 위치에 재방문이 가능함.
따라서 방문 검사 배열에 True/False 아닌 다른 정보를 저장해야 함.

------------------------------------------------------------------------------
예제 1) 방문여부 대신에 최단 거리를 기록 & 방문 기록 배열을 2개의 Case로 나누어 기록

조건 : 목적지 까지의 최단 거리 구하는데 갈 수 없는 벽을 1번 뚫고 지나갈 수 있다.
문제점 : 같은 위치에 도달하더라도 1.벽은 부순 경우와 2.벽을 부수지 않은 경우, 총 2가지 존재
해결법 : 
1. 벽 부순 경우와 2. 벽 안 부순 경우의 현재 위치까지의 최단거리를 각각 다른 방문 검사 배열에 저장
- 배열 1 : 벽은 부순 경우 현재 위치까지의 최단거리 저장
- 배열 2 : 벽을 부수지 않은 경우 현재 위치까지의 최단거리 저장

그리고 벽을 부쉈는지 여부(True/False)를 큐에 같이 저장해서 현재 상태를 확인 할 수 있게 한다.
벽을 부쉈다면 1번 배열, 안 부쉈다면 2번 배열의 정보를 사용한다

-----------------------------------------------------------------------------------
예제 2) 방문 여부 대신에 경로 자체를 기록

조건 : 최대한 많은 칸을 지나야하는데 각 칸에는 대문자 알파벳있다. 각 알파벳을 단 1번씩만 지나갈 수 있다.
문제점 : 똑같은 위치에 여러가지 경로를 거쳐서 올 수 있음 (알파벳을 다르게 지나서 도착)
해결법 : 경로 자체를 큐 또는 리스트에 저장한다. (경로는 문자열로)
똑같은 경로로 도달했으면 무시, 다른 경로로 도달했으면 큐 또는 리스트에 넣고 계속 진행
'''

