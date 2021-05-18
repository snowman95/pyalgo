import sys
board = [sys.stdin.readline().rstrip() for _ in range(8)]
cnt = 0
for i in range(8):
    start = 0
    if i %2 == 1:
        start = 1
    for j in range(start,8,2):
        if board[i][j] == 'F':
            cnt+=1
print(cnt)