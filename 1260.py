import sys
import collections

n,m,v = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    x,y = map(int, sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)
for a in arr:
    a.sort()

def dfs(cur, cnt, visited):
    visited[cur] = True
    sys.stdout.write(str(cur) + ' ')
    for i in arr[cur]:
        if not visited[i]:
            dfs(i,cnt+1,visited)
            
def bfs(start, cnt, visited):
    q = collections.deque([(start,cnt)])
    visited[start] = True
    while q:
        cur = q.popleft()
        sys.stdout.write(str(cur[0]) + ' ')
        for i in arr[cur[0]]:
            if not visited[i]:
                q.append((i, cur[1]+1))
                visited[i] = True

dfs(v,0,[False]*(n+1))
sys.stdout.write('\n')
bfs(v,0,[False]*(n+1))