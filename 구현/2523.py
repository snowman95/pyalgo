'''
별 찍기 - 13

'''
import sys
n = int(sys.stdin.readline())
for i in range(1,n+1):
    print('*'*i)
for i in range(1,n):
    print('*'*(n-i))