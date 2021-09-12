'''
이진 트리

이진트리 모양 초원에 늑대와 양
루트에서 출발하여 양을 수집
노드 방문마다 늑대/양이 나를 따라옴.

늑대 : 수집한 양의 수 <= 수집한 늑대 수 : 모든양 죽임
최대한 많은 양을 남기고 루트로 돌아와야 함.


[아이디어 회의]
그 게임이랑 비슷함
용사 level이랑 몬스터 level 비교해서 용사 level 이 더 크면 괜찮은거

1. 이진트리 구조를 굳이 생성할 필요 없을듯 함.
   인접리스트로 구성해도 무관할듯함.

2. 이걸 bfs로 한다고 가정해보자.
(양의수, 늑대의수, [방문안한 노드], [방문한 노드])

2. 양은 +, 늑대는 - 가중치로 가정한다면?
가는 방향을 +1/-1로 표기하고, 오는방향은 0으로 해서 사이클 가능하도록

이거 플로이드 워셜로 풀고
d[i][k]+d[k][i] 최소 되도록 구성한다면?!!!!!!!
아 근데 음의 사이클 생성 가능성 존재함.
그러면 양을 1000 값으로 주고, 늑대를 1 값으로 주도록 하셈

0->1 : +1000
1->0 : 0
0->8 : 1000
8->0 : 0
1->2 : 1000
1->4 : -1
4->3 : -1
4->6 : -1
6->5 : +1

각 노드에 있는 양 또는 늑대에 대한 정보가 담긴 배열 info,
2진 트리의 각 노드들의 연결 관계를 담은 2차원 배열 edges


[다시 아이디어 회의]
이거 우선순위 큐로는 못풀까?



'''

# import heapq

# parent = []
# node_score = []
# def update_parent(node_number, new_sheep, new_wolf):
#     global parent
#     global node_score
#     if node_score[node_number][0]-node_score[node_number][1] <= new_sheep-new_wolf:
#         node_score[node_number] = (new_sheep, new_wolf)
#         print("갱신", node_number, "번이", "양", new_sheep,"| 늑대", new_wolf)
#     if node_number == 0: 
#         return
#     update_parent(parent[node_number], new_sheep, new_wolf)
            

# def solution(info, edges):
#     global parent
#     global node_score
#     answer = 0
#     node_size = len(info)
#     tree = [[] for _ in range(node_size)]

#     # 부모가 -1이면 root임
#     parent = [-1] + [0] * (node_size-1)
#     for a,b in edges:
#         tree[a].append(b)
#         parent[b] = a

#     node_score = [(0,0)] * (node_size)
#     q = []
#     heapq.heappush(q,(-1,0,0))
#     while q:
#         sheep, wolf, node_num = heapq.heappop(q)
#         sheep = -sheep
#         update_parent(node_num, sheep, wolf)
#         for child in tree[node_num]:
#             if info[child] == 0: # 양
#                 q.append((-sheep-1,wolf,child))
#             else: #늑대
#                 if sheep <= wolf+1:
#                     q.append((0,wolf+1,child))
#                 else:
#                     q.append((-sheep,wolf+1,child))
#     answer = node_score[0][0]
#     print(answer)
#     return answer

# info= [0,0,1,1,1,0,1,0,1,0,1,1]
# edges= [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
# solution(info, edges)
import heapq

def solution(info, edges):
    global parent
    answer = 0
    node_size = len(info)
    tree = [[] for _ in range(node_size)]
    root_s = 0
    root_w = 0
    for a,b in edges:
        tree[a].append(b)

    q = []
    heapq.heappush(q,(-1,0,0))
    while q:
        sheep, wolf, node_num = heapq.heappop(q)
        sheep = -sheep
        if root_s - root_w < sheep - wolf:
            if info[node_num] == 0:
                root_s = sheep
                root_w = wolf
                q.append((-1,0,0))
            else:
                root_s = sheep 
                root_w = wolf +1
                q.append((-1,0,0))
        elif root_s - root_w > sheep - wolf:
            if info[node_num] == 0:
                sheep = root_s
                wolf = root_w
            else:
                sheep = root_s
                wolf = root_w +1
        else :
            break

        for child in tree[node_num]:
            if info[child] == 0: # 양
                q.append((-sheep-1,wolf,child))
            else: #늑대
                if sheep <= wolf+1:
                    q.append((0,wolf+1,child))
                else:
                    q.append((-sheep,wolf+1,child))
    answer = root_s-root_w
    return answer

info= [0,0,1,1,1,0,1,0,1,0,1,1]
edges= [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
solution(info, edges)