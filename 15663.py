import sys
import itertools
n,m = map(int, sys.stdin.readline().split())
arr = sorted(map(int, sys.stdin.readline().split()))
for p in sorted(set(itertools.permutations(arr,m))):
    for i in p:
        sys.stdout.write(str(i) + ' ')
    sys.stdout.write('\n')