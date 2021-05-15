import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()
start, end = 0,n-1
best = [int(1e10), 0,0]

while start < end:
    cur = abs(arr[start] + arr[end])
    if best[0] > cur:
        best = [cur, arr[start], arr[end]]
        
    next_end = abs(arr[start] + arr[end-1])
    next_start = abs(arr[start+1] + arr[end])
    if arr[start] + arr[end] == 0:
        break
    if next_start < next_end:
        start +=1
    elif next_start >= next_end:
        end-=1

print(best[1],best[2])