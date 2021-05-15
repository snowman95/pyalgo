import sys

n = int(sys.stdin.readline())
board = [sys.stdin.readline().rstrip() for _ in range(n)]
comp_result = []
def color_check(x,y,length):
    global color
    color = board[x][y]
    for i in range(length):
        for j in range(length):
            if board[x+i][y+j] != color:
                return '-1'
    return color
def compress(x,y,length):
    c = color_check(x,y,length)
    if c != '-1':
        comp_result.append(c)
    else:
        half = length//2
        comp_result.append('(')
        compress(x,y,half)
        compress(x,y+half,half)
        compress(x+half,y,half)
        compress(x+half,y+half,half)
        comp_result.append(')')

compress(0,0,n)
for i in comp_result:
    sys.stdout.write(i)