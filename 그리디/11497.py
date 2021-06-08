import sys,collections
T = int(sys.stdin.readline())
for t in range(T):
    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))
    l.sort(reverse=True)
    q = collections.deque([l[0]])
    for i in range(1,n):
        if i%2 == 1: q.append(l[i])
        else: q.appendleft(l[i])
    diff = abs(q[-1]-q[0])
    for i in range(0,n-1):
        diff = max(diff, abs(q[i]-q[i+1]))
    print(diff)