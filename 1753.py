import sys, heapq

INF = int(1e9)
v,e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]

for i in range(e):
    a,b,w = map(int, sys.stdin.readline().split())
    graph[a].append((w,b))

distance_arr = [INF] * (v+1)
distance_arr[k] = 0

heap = []
heapq.heappush(heap,(0,k))
while heap:
    dist, cur = heapq.heappop(heap)
    if distance_arr[cur] < dist:
        continue
    for n in graph[cur]:
        cost = dist + n[0]
        next = n[1]
        if distance_arr[next] > cost :
            distance_arr[next] = cost
            heapq.heappush(heap,(cost,next))

for i in range(1,v+1):
    if distance_arr[i] == INF:
        print("INF")
    else:
        print(distance_arr[i])