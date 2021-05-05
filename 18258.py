import sys
import collections
n = int(sys.stdin.readline())
com = [ tuple(sys.stdin.readline().split()) for i in range(n)]
q = collections.deque()

for c in com:
    if c[0] == 'push':
        q.append(c[1])
    elif c[0] == 'pop':
        if q: print(q.popleft())
        else : print(-1)
    elif c[0] == 'front':
        if q: print(q[0])
        else : print(-1)
    elif c[0] == 'back':
        if q : print(q[-1])
        else : print(-1)
    elif c[0] == 'size':
        print(len(q))
    elif c[0] == 'empty':
        if q: print(0)
        else : print(1)