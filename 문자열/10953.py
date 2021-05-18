import sys
T = int(sys.stdin.readline())
for t in range(T):
    print(sum(map(int, sys.stdin.readline().split(','))))