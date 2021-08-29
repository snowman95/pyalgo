'''
별 찍기 - 5

매순간 2만큼 커짐.
마지막 찍히는 개수는 1+2*(n-1)개
'''
import sys
n = int(sys.stdin.readline())
cur = "*"
for i in range(n):
    print(' '*(n-i-1), cur, sep='')
    cur += '**'