import sys, heapq

INF = int(1e9)
def dijkstra(start, dist_arr):
    global graph
    heap = []
    heapq.heappush(heap,(0,start))
    dist_arr[start] = 0
    while heap:
        dist, cur = heapq.heappop(heap)
        if dist_arr[cur] < dist:
            continue
        for n in graph[cur]:
            cost = dist + n[0]
            next = n[1]
            if dist_arr[next] > cost:
                dist_arr[next] = cost
                heapq.heappush(heap,(cost,next))
    return

n,e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(e):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

a,b = map(int, sys.stdin.readline().split())

dist_arr = [INF] * (n+1)
dijkstra(1, dist_arr)
start_to_a = dist_arr[a]
start_to_b = dist_arr[b]

dist_arr = [INF] * (n+1)
dijkstra(a, dist_arr)
a_to_b = dist_arr[b]
a_to_n = dist_arr[n]

dist_arr = [INF] * (n+1)
dijkstra(b, dist_arr)
b_to_a = dist_arr[a]
b_to_n = dist_arr[n]

ans = INF
if start_to_a != INF and a_to_b != INF and b_to_a != INF:
    ans = min(ans,start_to_a + a_to_b + b_to_n)
if start_to_b != INF and b_to_a != INF and a_to_n != INF:
    ans = min(ans,start_to_b + b_to_a + a_to_n)

if ans == INF:
    ans = -1
sys.stdout.write(str(ans))