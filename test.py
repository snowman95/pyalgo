import sys
board = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
x = 1
y = 1
board[x][y] = 9
while True:

    if y<9 and board[x][y+1] == 0:
        y+=1
        board[x][y] = 9
    elif y<9 and board[x][y+1] == 2:
        y+=1
        board[x][y] = 9
        break 
    elif x<9 and board[x+1][y] == 0:
        x+=1    
        board[x][y] = 9
    elif x<9 and board[x+1][y] == 2:
        x+=1
        board[x][y] = 9
        break 
    else:
        break
for x in range(10):
    for y in range(10):
        sys.stdout.write(str(board[x][y])+' ')
    sys.stdout.write('\n')


'''
이차원 리스트 쉽게 만드는 방법
d = [[0] * 19 for _ in range(19)]

[list(map(int,sys.stdin.readline().split())) for i in range(19)]


import math
a,b,c = map(int,sys.stdin.readline().split())
print(math.lcm(a,b,c))

'''
#w,h,b= map(int,sys.stdin.readline().split())
#n = int(sys.stdin.readline())

# n = int(input())
#a = [int(sys.stdin.readline()) for i in range(n)] 
#f = filter(lambda x : x%2==0, a)
# for i in range(1,n+1): 
#     sys.stdout.write(str(i)+'\n')x