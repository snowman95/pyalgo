import sys
n = int(sys.stdin.readline())
a,b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
board = [[] *n for _ in range(n+1)]
for i in range(m):
    x,y = map(int, sys.stdin.readline().split())
    board[x].append(y)
    board[y].append(x)

chonsu_arr = [0]*(n+1)
def dfs(num, chonsu):
    global board
    chonsu_arr[num] = chonsu
    
    for i in board[num]:
        if chonsu_arr[i] == 0:
            dfs(i, chonsu+1)

dfs(a,0)
if chonsu_arr[b] == 0:
    print(-1)
else :
    print(chonsu_arr[b])