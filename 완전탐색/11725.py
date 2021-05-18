import sys, collections
n = int(sys.stdin.readline())
board = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    board[a].append(b)
    board[b].append(a)

parent_arr = [0]*(n+1)

q = collections.deque([(1,-1)])
while q:
    cur, parent = q.popleft()
    parent_arr[cur] = parent
    for i in board[cur]:
        if parent_arr[i] == 0:
            q.append((i, cur))

for i in range(2,n+1):
    print(parent_arr[i])