import sys
n = int(sys.stdin.readline())
star = [ '*'*(n-i) for i in range(n)]
for i in star:
    print(i)