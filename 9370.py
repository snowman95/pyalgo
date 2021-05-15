import sys, heapq

INF = int(1e9)
def dijkstra(start, distance_arr):
    global graph
    heap = []
    heapq.heappush(heap,(0,start))
    distance_arr[start] = 0
    while heap:
        dist, cur = heapq.heappop(heap)
        if distance_arr[cur] < dist:
            continue
        for n in graph[cur]:
            cost = dist + n[0]
            next = n[1]
            if distance_arr[next] > cost:
                distance_arr[next] = cost
                heapq.heappush(heap,(cost,next))
    return

T = int(sys.stdin.readline())
for test_case in range(T):
    n,m,t = map(int, sys.stdin.readline().split())
    s,g,h = map(int, sys.stdin.readline().split())
    
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        a,b,d = map(int, sys.stdin.readline().split())
        if (a == h and b == g) or (a == g and b == h):
            d -= 0.1
        graph[a].append((d,b))
        graph[b].append((d,a))

        
    dist_candidate = [int(sys.stdin.readline()) for i in range(t)]
    dist_arr = [INF] * (n+1)
    dijkstra(s, dist_arr)
    ans = []
    for can in dist_candidate:
        if isinstance(dist_arr[can],float):
            ans.append(can)

    for a in sorted(ans):
        sys.stdout.write(str(a) + ' ')
    sys.stdout.write('\n')