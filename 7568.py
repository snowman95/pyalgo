import sys
n = int(sys.stdin.readline())
man = [[0,0] for _ in range(n)]
for i in range(n):
    man[i] = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    rank = n
    for j in range(n):
        if i==j :
            continue
        if man[i][0] >= man[j][0] or  man[i][1] >= man[j][1]:
            rank -=1
    sys.stdout.write(str(rank) + " ")