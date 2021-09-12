'''
위상정렬 
O(V + E)
'''

import collections

v, e = map(int, input().split())
indegree = [0] * (v + 1) # 모든 노드의 진입차수 (초기화: 0)
graph = [[] for i in range(v + 1)] # 연결 리스트(간선 정보)

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # a→b 이동가능
    indegree[b] += 1   # 진입 차수 1 증가

def topology_sort():
    result = []
    q = collections.deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        # 내가 다음노드로 진입하기 때문에 -1하는것.
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()