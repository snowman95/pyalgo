import sys
import itertools
n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

for p in list(itertools.product(arr,repeat=m)):
    for i in p:
        sys.stdout.write(str(i) + ' ')
    sys.stdout.write('\n')