import sys

n = int(sys.stdin.readline())
fibo = [1,1] + [0]*(n)
for i in range(2,n+2):
    fibo[i] = fibo[i-1]+fibo[i-2]

print((fibo[n]+fibo[n-1])*2)