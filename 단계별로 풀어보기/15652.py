import sys
import itertools
n,m = map(int, sys.stdin.readline().split())
for p in list(itertools.combinations_with_replacement(range(1,n+1),m)):
    for i in p:
        sys.stdout.write(str(i) + ' ')
    sys.stdout.write('\n')