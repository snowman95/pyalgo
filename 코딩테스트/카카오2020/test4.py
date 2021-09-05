'''
두 사람은 S에서 출발해서 각각 A,B로 가려함

- 양방향 그래프
- 노드(지점 번호) 3~200개
- 간선(택시요금) 1~10만
- 출력 : 최저 택시요금

2가지 경우 존재
1. 같이 택시 탄다 -> 각각 따로 간다
2. 각각 따로 탄다

이거 A-> B로 가는 경로 구하고,
경로상의 모든 노드에서 S로 향하면 됨!!
그 중 최저 비용 구하면 끝.

'''
# import collections, sys
# MAX_NUM = 100002
# board = [[] for _ in range(MAX_NUM)]

# def a_to_b_bfs(start, end):
#     global board
#     total_cost = sys.maxsize
#     total_trace = []
#     q = collections.deque([(start, 0, [start])])

#     visited = [sys.maxsize] * MAX_NUM
#     visited[start] = 0
#     while q:
#         node, cost, trace = q.popleft()
#         if node == end:
#             if total_cost > cost:
#                 total_cost = cost
#                 total_trace = trace
#             continue
#         for next_node,connect_cost in board[node]:
#             next_cost = cost + connect_cost
#             if visited[next_node] > next_cost:
#                 visited[next_node] = next_cost
#                 q.append((next_node, next_cost, trace+[next_node]))
#     return (total_cost, total_trace)

# def node_to_node_bfs(start, end):
#     global board
#     total_cost = sys.maxsize
#     q = collections.deque([(start, 0)])
#     visited = [sys.maxsize] * MAX_NUM
#     visited[start] = 0
#     while q:
#         node, cost = q.popleft()
#         if node == end:
#             if total_cost > cost:
#                 total_cost = cost
#             continue
#         for next_node,connect_cost in board[node]:
#             next_cost = cost + connect_cost
#             if visited[next_node] > next_cost:
#                 visited[next_node] = next_cost
#                 q.append((next_node, next_cost))
#     return total_cost

# def solution(n, s, a, b, fares):
#     answer = 0
#     for c,d,f in fares:
#         board[c].append((d,f))
#         board[d].append((c,f))

#     # 1. a->b 경로가 존재하는 경우
#     a_to_b_cost, a_to_b_trace = a_to_b_bfs(a,b)
#     answer = a_to_b_cost
#     # a->b 경로 상 s가 포함안되는 경우
#     if s not in a_to_b_trace:
#         # a->b 경로 상 모든 위치에서 시작
#         if a_to_b_cost != sys.maxsize:
#             node_to_s_cost= sys.maxsize
#             for node in a_to_b_trace:
#                 node_to_s_cost = min(node_to_s_cost, node_to_node_bfs(node, s))
#             answer = node_to_s_cost + a_to_b_cost
#         # 2. s->a, s->b 따로 구한 것
#         answer = min(answer, node_to_node_bfs(s,a) + node_to_node_bfs(s,b))

#     print(answer)
#     return answer



INF = 100005
def solution(n, s, a, b, fares):
    matrix = [[INF for j in range(n)] for i in range(n)]
    for i in range(n):
        matrix[i][i] = 0

    for c,d,cost in fares:
        matrix[c-1][d-1] = cost
        matrix[d-1][c-1] = cost

    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    return min(matrix[s-1][k] + matrix[k][a-1] + matrix[k][b-1] for k in range(n))
n=6
s=4
a=6
b=2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
solution(n,s,a,b,fares)