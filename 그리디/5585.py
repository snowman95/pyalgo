import sys
n = int(sys.stdin.readline())
coin = (500,100,50,10,5,1)
n = 1000-n
cnt = 0
for c in coin:
    if n>=c:
        tmp = n//c
        n-=tmp*c
        cnt += tmp
print(cnt)