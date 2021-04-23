import sys
import itertools
n,m = map(int, sys.stdin.readline().split())
for p in list(itertools.product(range(1,n+1), repeat=m)):
    for i in p:
        sys.stdout.write(str(i) + ' ')
    sys.stdout.write('\n')