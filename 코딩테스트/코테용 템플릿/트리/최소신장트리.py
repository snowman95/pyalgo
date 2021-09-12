'''
최소 신장 트리 (MST)

사이클형성하지 않고 이어진 트리 중 가중치 합이 최소인것

크루스칼 알고리즘 O(ElogV)
모든 정점을 독립적인 집합으로 만든다.
모든 간선을 비용을 기준으로 정렬하고, 비용이 작은 간선부터 양 끝의 두 정점을 비교한다.
두 정점의 최상위 정점을 확인하고, 서로 다를 경우 두 정점을 연결한다.

'''
parent = {}
rank = {}
# 해당 정점의 최상위 정점을 찾는다.
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]
# 두 정점을 연결한다.
def union(v, u):
    root1 = find(v)
    root2 = find(u)
    if root1 != root2:
        # 짧은 트리의 루트가 긴 트리의 루트를 가리키게 만드는 것이 좋다.
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal():
    mst = []
    # 정점을 독립적인 집합으로 만든다.
    for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        parent[v] = v
        rank[v] = 0
    
    # 가중치, A->B 순서
    edges = [(7, 'A', 'B'),(5, 'A', 'D'),(7, 'B', 'A')]
    edges.sort()

    for edge in edges:
        weight, v, u = edge
        # 부모 같지 않으면 하나의 연합으로 묶음
        if find(v) != find(u):
            union(v, u)
            mst.append(edge)
    return mst
            
print( kruskal() )


'''
프림 알고리즘
'''
INF = 999
# 인접행렬 형태. 1->2비용이 몇 이렇게 되어있는 상태
adj_mat = [[0, 29, INF, INF, INF, 10, INF],
           [29, 0, 16, INF, INF, INF, 15],
           [INF, 16, 0, 12, INF, INF, INF],
           [INF, INF, 12, 0, 22, INF, 18],
           [INF, INF, INF, 22, 0, 27, 25],
           [10, INF, INF, INF, 27, 0, INF],
           [INF, 15, INF, 18, 25, INF, 0]]

node_num = len(adj_mat)
visited = [False] * node_num
distances = [INF] * node_num

def get_min_node(node_num):
    # 미방문 노드 v에 저장
    for i in range(node_num):
        if not visited[i]:
            v = i
            break
    for i in range(node_num):
        # 미방문에 거리가 더 짧은 정점 발견시 교체
        if not visited[i] and distances[i] < distances[v]:
            v = i
    return v

def prim(start, node_num):
    # distances 배열과 visted 배열 초기화
    for i in range(node_num):
        visited[i] = False
        distances[i] = INF

    # 시작노드의 distance 값을 0으로 초기화
    distances[start] = 0
    for i in range(node_num):
        print("--------------------")
        node = get_min_node(node_num)
        visited[node] = True

        for j in range(node_num):
            if adj_mat[node][j] != INF:
                if not visited[j] and adj_mat[node][j] < distances[j]:
                    distances[j] = adj_mat[node][j]
        print("distances: ", distances)

print(prim(0, node_num))
print("distances: ", distances)
print("minimum cost: ", sum(distances))