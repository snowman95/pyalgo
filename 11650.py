import sys
n = int(sys.stdin.readline())
location = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
location.sort()
for lo in location:
    sys.stdout.write(str(lo[0]) + ' ' + str(lo[1]) +'\n')