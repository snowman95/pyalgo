import sys
n,m = map(int,sys.stdin.readline().split())
target = list(map(int,sys.stdin.readline().split()))
s = 0
e = 2**31-1
while s <= e:
    mid = (s+e)//2
    cnt = 0
    for t in target:
        if t > mid:
            cnt += t-mid
    if m <= cnt:
        s = mid+1
    else:
        e = mid-1
print(e)