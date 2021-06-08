# import sys
# n,b = map(int, sys.stdin.readline().split())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# visited = [False]*(b+1)
# visited[1] = True
# dp = [[[0]*n for _ in range(n)] for _ in range(b+1)]
# ans = arr
# dp[1] = arr
# def cross(dp, s1, s2):
#     global n
#     for x in range(n):
#         for y in range(n):
#             for z in range(n):
#                 dp[x][y] += (s1[x][z]*s2[z][y])
#             dp[x][y] %= 1000
#     return 

# def func(step):
#     print("step :", step)
#     if visited[step]:
#         return dp[step]
#     if step <= 1:
#         return arr
#     last = step%2
#     half = step//2
#     visited[step] = True
#     if last == 1:
#         cross(dp[step], func(step-1), func(last))
#     else:
#         cross(dp[step], func(half), func(half))
#     return dp[step]

# func(b)
# for i in range(n):
#     for j in range(n):
#         sys.stdout.write(str(dp[b][i][j]) + ' ')
#     sys.stdout.write('\n')

import sys
n,b = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = arr
def cross(s1, s2):
    tmp = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            for z in range(n):
                tmp[x][y] += (s1[x][z]*s2[z][y])
            tmp[x][y] %= 1000
    return tmp

def func(step):
    pre = []
    if step <= 1:
        return arr
    if step%2 == 0:
        pre = func(step//2)
        return cross(pre, pre)
    else:
        pre = func(step-1)
        return cross(pre, arr)
    print("step :", step, pre)
    return pre

if b == 1:
    for i in range(n):
        for j in range(n):
            sys.stdout.write(str(ans[i][j]%1000) + ' ')
        sys.stdout.write('\n')
else :    
    ans = func(b)
    for i in range(n):
        for j in range(n):
            sys.stdout.write(str(ans[i][j]) + ' ')
        sys.stdout.write('\n')