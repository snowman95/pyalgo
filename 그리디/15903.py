import sys
n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    arr.sort()
    arr[0] = sum(arr[0:2])
    arr[1] = arr[0]
print(sum(arr))