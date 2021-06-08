import sys
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
cur = arr[-1]
cnt = 0
for i in range(n-2,-1,-1):
    if cur <= arr[i]:
        sub = arr[i]-cur+1
        cnt += sub
        cur = arr[i]-sub
    else:
        cur = arr[i]
print(cnt)