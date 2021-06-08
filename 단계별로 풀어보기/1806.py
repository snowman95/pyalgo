import sys
n,s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
MAX = int(1e10)

start, end, summary, min_len = 0,0,0,MAX
for start in range(n):
    while summary < s and end < n:
        summary += arr[end]
        end+=1
    if summary >= s:
        min_len = min(min_len, end-start)
        summary -= arr[start]

if min_len == MAX:
    min_len = 0
print(min_len)