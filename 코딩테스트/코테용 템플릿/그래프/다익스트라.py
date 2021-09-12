'''
최소 비용만 구하기
'''
import sys, heapq
INF = int(1e9) #수정필요 (노드수 * 최대비용 + 1)
n,m,k,x = map(int,sys.stdin.readline().split())
board = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    board[a].append(b)

dist_arr = [INF]*(n+1)
dist_arr[x]=0
q = []
heapq.heappush(q, (0,x))
while q:
    dist, cur = heapq.heappop(q)
    if dist_arr[cur] < dist:
        continue

    for next in board[cur]:
        if dist_arr[next] > dist+1:
            dist_arr[next] = dist+1
            heapq.heappush(q, (dist+1,next))

cnt = 0
for i in range(1,n+1):
    if dist_arr[i] == k:
        print(i)
        cnt+=1
if cnt==0:
    print(-1)





'''
최소 비용의 경로까지 저장
'''
import sys, heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = n*100000+1
arr = [[INF] * n for _ in range(n)]
dist_arr = [INF]*n
trace_arr = [[] for _ in range(n)]

for i in range(m):
    s,e,cost = map(int,sys.stdin.readline().split())
    arr[s-1][e-1] = min(arr[s-1][e-1], cost)

for i in range(n):
    trace_arr[i].append(i+1)

s,e = map(int,sys.stdin.readline().split())
s,e = (s-1, e-1)
dist_arr[s] = 0

q = []
heapq.heappush(q, (0, s))
while q:
    cur_dist, cur_pos = heapq.heappop(q)
    if dist_arr[cur_pos] < cur_dist:
        continue
    for i in range(n):
        if arr[cur_pos][i] != INF :
            next_pos, move_dist = (i, arr[cur_pos][i])
            next_dist = cur_dist + move_dist
            if dist_arr[next_pos] > next_dist:
                dist_arr[next_pos] = next_dist
                heapq.heappush(q, (next_dist, next_pos))
                trace_arr[next_pos] = trace_arr[cur_pos] + [next_pos+1]

print(dist_arr[e])
print(len(trace_arr[e]))
for i in trace_arr[e]:
    sys.stdout.write(str(i)+ ' ')