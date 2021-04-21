import sys
import bisect
n = int(sys.stdin.readline())
position = list(map(int,sys.stdin.readline().split()))
d_position = dict()
u_position = sorted(set(position))
for p in position:
    if p in d_position:
        sys.stdout.write(d_position[p] + ' ')
    else :
        d_position[p] = str(bisect.bisect_left(u_position, p))
        sys.stdout.write(d_position[p] + ' ')