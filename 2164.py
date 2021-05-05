import sys
import collections
n = int(sys.stdin.readline())
q = collections.deque(list(range(1,n+1)))

while n > 1:
    q.popleft()
    n-=1
    if n>1:
        q.append(q.popleft())
print(q.pop())