import sys
T = int(sys.stdin.readline())
for i in range(T):
    R, S = sys.stdin.readline().rstrip('\n').split()
    for s in S:
        for j in range(int(R)):
            sys.stdout.write(s)
    sys.stdout.write('\n')