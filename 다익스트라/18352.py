# import sys, collections

# n,m,k,x = map(int,sys.stdin.readline().split())
# board = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int,sys.stdin.readline().split())
#     board[a].append(b)

# visited = [0]*(n+1)
# q = collections.deque([(x,0)])
# visited[x] = 1
# while q:
#     cur, dist = q.popleft()
#     for i in board[cur]:
#         if visited[i] == 0:
#             visited[i] = 1
#             if dist+1 == k: visited[i] = 10
#             elif dist+1 < k:
#                 q.append((i,dist+1))

# cnt = 0
# for i in range(1,n+1):
#     if visited[i] == 10:
#         print(i)
#         cnt+=1
# if cnt==0:
#     print(-1)


import sys, heapq
MAX = int(1e9)
n,m,k,x = map(int,sys.stdin.readline().split())
board = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    board[a].append(b)

dist_arr = [MAX]*(n+1)
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