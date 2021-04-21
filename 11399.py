import sys

import itertools
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
print(sum(itertools.accumulate(arr)))

'''
(1~N)번호적힌 N명사람 줄섬. 
pi = i번 인출시간

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
result = sum([sum(arr[:i+1]) for i in range(n)])

print(result)
'''