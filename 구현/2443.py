'''
별 찍기 - 6

1 - 9
2 - 7
3 - 5
4 - 3
5 - 1
'''
import sys
n = int(sys.stdin.readline())
cur = "*" *(2*(n-1)) +'*'

for i in range(n):
    cur = "*" *(2*(n-i-1)) +'*'
    print(' '*i, cur, sep='')