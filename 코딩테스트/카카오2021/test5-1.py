'''
트리를 만들면서 진행할거임.

'''

def solution(info, edges):
    answer = 0    
    parent = []
    node_score = []
    node_size = len(info)
    tree = [[] for _ in range(node_size)]

    # 부모가 -1이면 root임
    parent = [-1] + [0] * (node_size-1)
    for a,b in edges:
        tree[a].append(b)
        parent[b] = a

    node_score = [(0,0)] * (node_size)
    q = []
    heapq.heappush(q,(-1,0,0))
    while q:
        sheep, wolf, node_num = heapq.heappo
    return answer