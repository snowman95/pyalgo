import sys,math
n =int(sys.stdin.readline())
arr = []
prime_arr = [False,False] + [True]*(n-1)
for i in range(2, n+1):
    if prime_arr[i] :
        for j in range(2*i, n+1, i):
            prime_arr[j] = False

size = 0
for i in range(n+1):
    if prime_arr[i]:
        arr.append(i)
        size+=1

start, end, summary, cnt = 0,0,0,0
for start in range(size):
    while summary < n and end < size:
        summary += arr[end]
        end+=1
    if summary == n:
        cnt +=1
    summary -= arr[start]

print(cnt)