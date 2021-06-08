import sys
import itertools
n,m = map(int, sys.stdin.readline().split())
arr = sorted(map(int, sys.stdin.readline().split()))
for p in sorted(set(itertools.combinations_with_replacement(arr,m))):
    for i in p:
        sys.stdout.write(str(i) + ' ')
    sys.stdout.write('\n')