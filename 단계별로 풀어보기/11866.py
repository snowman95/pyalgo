import sys, collections
n,k = map(int, sys.stdin.readline().split())
q =collections.deque(list(range(1,n+1)))
arr = []
while q:
    for i in range(k-1):
        q.append(q.popleft())
    arr.append(q.popleft())
sys.stdout.write('<')
for i in range(n-1):
    sys.stdout.write(str(arr[i]) + ', ')
sys.stdout.write(str(arr[-1]))
sys.stdout.write('>')