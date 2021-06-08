import sys, collections
n = int(sys.stdin.readline())
com = [tuple(sys.stdin.readline().split()) for _ in range(n)]
q= collections.deque()
for c in com:
    if c[0] == 'push_back':
        q.append(c[1])
    elif c[0] == 'push_front':
        q.appendleft(c[1])
    elif c[0] == 'pop_front':
        if q: print(q.popleft())
        else : print(-1)
    elif c[0] == 'pop_back':
        if q: print(q.pop())
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