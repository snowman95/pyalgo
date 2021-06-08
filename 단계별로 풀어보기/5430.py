import sys, collections
T = int(sys.stdin.readline())
for t in range(T):
    com = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    re = False
    error = False
    if n == 0:
        tmp_arr = sys.stdin.readline()
        if 'D' in com:
            print('error')
        else:
            print('[]')
    else :
        tmp_arr = sys.stdin.readline().rstrip()
        q = collections.deque(tmp_arr[1:-1].split(','))
        for c in com:
            if c == 'R':
                re ^= True
            else :
                if not q : 
                    error = True
                    continue
                if re : q.pop()
                else : q.popleft()
    
        if error:
            print('error')
        else:
            if q: 
                if re : q.reverse()
                sys.stdout.write('['+','.join(q) + ']\n')
            else :
                sys.stdout.write('[]\n')