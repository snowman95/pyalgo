import sys, collections
n, m = map(int,sys.stdin.readline().split())
pos = map(int, sys.stdin.readline().split())
q = collections.deque(list(range(1,n+1)))
cnt = 0
for p in pos:
    idx = q.index(p)
    if idx != 0:
        if n//2 >= idx :
            cnt += idx
            idx = -idx
        else : 
            idx = n-idx
            cnt += idx
        q.rotate(idx)
    q.popleft()
    n-=1
print(cnt)