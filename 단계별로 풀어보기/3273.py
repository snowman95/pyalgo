import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
x = int(sys.stdin.readline())
arr.sort()
start, end = 0,n-1
cnt = 0
while start < end:
    total = arr[start] + arr[end]
    if total > x:
        end-=1
    elif total < x:
        start+=1
    else:
        start+=1
        cnt+=1

print(cnt)