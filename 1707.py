import sys
import collections

def bfs(pos):
    global red_blue
    global graph
    q = collections.deque([pos])
    red_blue[pos] = 1
    while q:
        p = q.popleft()
        for v in graph[p]:
            if red_blue[v] == 0:
                red_blue[v] = -red_blue[p]
                q.append(v)
            else:
                if red_blue[v] == red_blue[p]:
                    return False
    return True

T = int(sys.stdin.readline())
for i in range(T):
    v,e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v)]
    red_blue = [0]*v
    for i in range(e):
        x,y = map(int, sys.stdin.readline().split())
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)
            
    ans = True
    for i in range(v):
        if red_blue[i] == 0:
            if not bfs(i):
                ans = False
                break
    if ans: print('YES')
    else: print('NO')