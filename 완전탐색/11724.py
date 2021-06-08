import sys
n,m=map(int,sys.stdin.readline().split())
link = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    u,v = map(int,sys.stdin.readline().split())
    link[u].append(v)
    link[v].append(u)

cnt = 0

def dfs(num):
    global visited
    visited[num] = True
    for item in link[num]:
        if not visited[item]:
            visited[item] = True
            dfs(item)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt +=1
print(cnt)