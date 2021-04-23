import sys
import itertools
board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zero_pos = [(x,y) for x in range(9) for y in range(9) if board[x][y] == 0]
z_len = len(zero_pos)
offset = list(itertools.product([1,-1,0],repeat=2))
offset_pos = [1]*3+[4]*3+[7]*3
finished = False
def choice(x,y):
    nums = list(range(1,10))
    for n in range(9):
        if board[x][n] in nums:
            nums.remove(board[x][n])
        if board[n][y] in nums:
            nums.remove(board[n][y])
    for off in offset:
        dx = offset_pos[x]+off[0]
        dy = offset_pos[y]+off[1]
        if board[dx][dy] in nums:
            nums.remove(board[dx][dy])
    return nums

def dfs(cur):
    global finished
    if finished == True :
        return
    if cur == z_len:
        for item in board:
            print(*item)
        finished = True
        return
    else:
        (x,y) = zero_pos[cur]
        for c in choice(x,y):
            board[x][y] = c
            dfs(cur+1)
            board[x][y] = 0
dfs(0)