import sys
import math
'''
8~50크기의 체스판을 8x8로 잘라서 격자무늬로 만들거임
아무대나 잘라도 됨.
대신에 다시 칠할부분이 최소가 되는 개수

세로로 [0:8] ~ [n-8:n]
가로로 [0:8] ~ [m-8:m] 까지 이동

'''
type1 = 'BWBWBWBW'
type2 = 'WBWBWBWB'
n,m = map(int, sys.stdin.readline().split())
board = ['a' * m for _ in range(n)]
for i in range(n):
    board[i] = sys.stdin.readline().rstrip('\n')

ans = math.inf
for i in range(0, n-8+1):
    for j in range(0, m-8+1):
        type1_diff = 0
        type2_diff = 0
        for row in range(0,8):
            slice_board = board[i+row][j:j+8]
            for r in range(0,8):
                check_type = ''
                if row%2 == 1: 
                    check_type = type1
                else : 
                    check_type = type2
                if check_type[r] != slice_board[r]:
                    type1_diff +=1
            for r in range(0,8):
                check_type = ''
                if row%2 == 0: 
                    check_type = type1
                else :  
                    check_type = type2
                if check_type[r] != slice_board[r]:
                    type2_diff +=1
        ans = min(ans,min(type1_diff, type2_diff))
print(ans)