import sys
k,n = map(int,sys.stdin.readline().split())
target = [int(sys.stdin.readline()) for _ in range(k)]
s = 0
e = 2**31-1
while s <= e:
    mid = (s+e)//2
    cnt = 0
    for t in target:
        cnt += (t // mid)
    if n <= cnt:
        if s == mid:
            break
        s = mid+1
    else:
        e = mid-1
print(e)