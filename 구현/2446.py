import sys
n = int(sys.stdin.readline())

cnt = 2*(n-1)+1
for i in range(1,cnt+1):
    if i<=n:
        print(" "*(i-1) + "*"*(2*(n-i)+1))
    else:
        print(" "*(cnt-i) + "*"*(2*(i-n)+1))