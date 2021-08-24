'''
순열 사이클

1~N까지의 정수 N개
1  2  3  4  5  6  7  8
3, 2, 7, 8, 1, 4, 5, 6

순번→자신 으로 향하는 사이클형성
visited = [False]*(n+1)
for i in range(n):
    if not visited[n]:
        bfs()
        cycle_cnt +=1

1~N 까지의 숫자라서 무조건 사이클 형성하게 되어있음.
그림 몇 번 그려보면 이해됨
'''
import sys, collections

def bfs(start, arr, visited):
    q = collections.deque([start])
    while q:
        cur = q.popleft()
        visited[cur] = True
        next = arr[cur]
        if not visited[next]:
            q.append(next)
        
T = int(sys.stdin.readline())
for t in range(T):
    n = int(sys.stdin.readline())
    arr = [0]+list(map(int, sys.stdin.readline().split()))
    visited = [False]*(n+1)
    cycle_cnt = 0
    for i in range(1,n+1):
        if not visited[i]:
            bfs(i, arr, visited)
            cycle_cnt +=1
    print(cycle_cnt)