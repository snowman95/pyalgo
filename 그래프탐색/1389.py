import sys, collections
n,m = map(int,sys.stdin.readline().split())
user = [[] *(n+1) for _ in range(n+1)]
min_link_cnt = (int(1e9),0)
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    user[a].append(b)
    user[b].append(a)

def bfs(start):
    global min_link_cnt, user
    q = collections.deque([(start,1)])
    visited = [False]*(n+1)
    visited[start] = True
    link_cnt = 0
    while q:
        cur,link = q.popleft()
        for next in user[cur]:
            if not visited[next]:
                visited[next]=True
                link_cnt+=link
                q.append((next,link+1))

    if min_link_cnt[0] >= link_cnt:
        if min_link_cnt[0] == link_cnt :
            if min_link_cnt[1] > start :
                min_link_cnt[1] = start
        else:
            min_link_cnt= (link_cnt, start)
for i in range(1,n+1):
    bfs(i)
print(min_link_cnt[1])