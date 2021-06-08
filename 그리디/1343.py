import sys
board = sys.stdin.readline().rstrip().split('.')
xcnt = 0
new_board = []
valid = True
for i in board:
    size = len(i)
    if size %2 == 1:
        valid=False
        break
    else:
        for a in range(size//4):
            new_board.append('AAAA')
        if size%4:
            new_board.append('BB')
    new_board.append('.')

if valid:
    if board[-1] != '.':
        new_board.pop()
    print(''.join(new_board))
else:
    print(-1)