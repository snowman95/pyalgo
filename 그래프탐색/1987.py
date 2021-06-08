# import sys, string
# sys.setrecursionlimit(30000)
# r,c = map(int, sys.stdin.readline().split())
# board = [sys.stdin.readline().rstrip() for _ in range(r)]
# visited = [[False] * c for _ in range(r)]
# visited_alpha = [False] * len(string.ascii_uppercase)
# A = ord('A')
# dx = (0,0,1,-1)
# dy = (1,-1,0,0)
# max_cnt = 0

# def dfs(x,y, cnt):
#     global visited, visited_alpha, max_cnt,r,c
#     max_cnt = max(max_cnt, cnt)
#     for i in range(4):
#         xx = dx[i]+x
#         yy = dy[i]+y
#         if xx>=0 and yy>=0 and xx<r and yy<c and not visited[xx][yy]:
#             alpha = ord(board[xx][yy]) - A
#             if  not visited_alpha[alpha]:
#                 visited_alpha[alpha] = True
#                 visited[xx][yy] = True
#                 dfs(xx,yy,cnt+1)
#                 visited_alpha[alpha] = False
#                 visited[xx][yy] = False

# visited[0][0]=True
# visited_alpha[ord(board[0][0]) - A] = True
# dfs(0,0,1)
# print(max_cnt)


# import sys, string
# r,c = map(int, sys.stdin.readline().split())
# board = [sys.stdin.readline().rstrip() for _ in range(r)]
# dx = (0,0,1,-1)
# dy = (1,-1,0,0)
# max_cnt = 1
# queue = set([(0, 0, board[0][0])])
# while queue and max_cnt < len(string.ascii_uppercase):
#     x, y, history = queue.pop()
#     for i in range(4):
#         xx, yy = dx[i]+x, dy[i]+y
#         if xx>=0 and yy>=0 and xx<r and yy<c and board[xx][yy] not in history:
#             queue.add((xx, yy, history + board[xx][yy]))
#             max_cnt = max(max_cnt, len(history) + 1)

# print(max_cnt)

# import sys, string
# r,c = map(int, sys.stdin.readline().split())
# board = [sys.stdin.readline().rstrip() for _ in range(r)]
# dx = (0,0,1,-1)
# dy = (1,-1,0,0)
# A  = ord('A')
# max_cnt = 1 
# bit = 1<<(ord(board[0][0])-A)
# queue = set([(0, 0, 1, bit)])
# while queue and max_cnt < len(string.ascii_uppercase):
#     x, y, cnt, cur_bit = queue.pop()
#     for i in range(4):
#         xx, yy = dx[i]+x, dy[i]+y
#         if 0<=xx<r and 0<=yy<c: 
#             seq = ord(board[xx][yy])-A
#             if cur_bit & (1<<seq) == 0 :
#                 queue.add((xx, yy, cnt+1, cur_bit | 1<<seq))
#                 max_cnt = max(max_cnt, cnt+1)

# print(max_cnt)

# import sys, string
# r,c = map(int, sys.stdin.readline().split())
# board = [sys.stdin.readline().rstrip() for _ in range(r)]
# visited = [[]*c for _ in range(r)]
# dx = (0,0,1,-1)
# dy = (1,-1,0,0)
# A  = ord('A')
# max_cnt = 1 
# bit = 1<<(ord(board[0][0])-A)
# queue = set([(0, 0, 1, bit)])
# while queue and max_cnt < len(string.ascii_uppercase):
#     x, y, cnt, cur_bit = queue.pop()
#     for i in range(4):
#         xx, yy = dx[i]+x, dy[i]+y
#         if 0<=xx<r and 0<=yy<c: 
#             seq = ord(board[xx][yy])-A
#             if cur_bit & (1<<seq) == 0 :
#                 queue.add((xx, yy, cnt+1, cur_bit | 1<<seq))
#                 max_cnt = max(max_cnt, cnt+1)

# print(max_cnt)

import sys
r,c = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
visited = [[[] for _ in range(c)] for _ in range(r)]
result = 0
dx = (-1,1,0,0)
dy = (0,0,1,-1)
A  = ord('A')
q = ([(0,0,1,1<<(ord(board[0][0])-A))])

while q and result < 26:
    x, y, cnt, cur_bit = q.pop()
    result = max(result, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0<= ny <c:
            seq = ord(board[nx][ny])-A
            if cur_bit & (1<<seq) == 0 :
                next_bit = cur_bit | 1<<seq
                print("---------------------------")
                print("nx,ny",nx,ny, bin(next_bit))
                for i in range(r):
                    for j in range(c):
                        if c[i][j] :
                            sys.stdout.write(str(bin(visited[i][j])) + ' ')
                        else:
                            sys.stdout.write("X ")
                    sys.stdout.write('\n')

                if visited[nx][ny] != next_bit:
                    print("추가됨")
                    visited[nx][ny] = next_bit
                    q.append((nx,ny,cnt+1,next_bit))
print(result)