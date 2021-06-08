import sys
x,y = map(int, sys.stdin.readline().split())
ans = 1
if x-y < y:
    y = x-y
for i in range(y):
    ans *= (x-i)
for i in range(2,y+1):
    ans //= i
print(ans%10007)