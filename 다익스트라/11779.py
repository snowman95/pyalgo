'''
최소비용 구하기 2

도시 n(1~1000)
연결버스 m(1~100,000)
A->B 도시 가는 최소 비용과 그 경로를 출력하시오.


알고리즘 : 다익스트라
시간복잡도 : OK
import math
print((1000+100000)*math.log(1000) < 20000000) True 확인

이 문제는 최소비용경로를 저장해야함.
다익스트라는 방문안된 곳을 탐욕적으로 갱신하는 그리드 알고리즘 이므로
해당 노드마다 방문 기록을 남기고,
다음 노드에 = 이전 방문기록 + 현재위치 이렇게 갱신할 수 있을 것으로 보임.

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