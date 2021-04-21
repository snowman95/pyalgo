import sys
def prime_check(n):
    c = [False,False] + [True]*(n-1)
    for i in range(2,n+1):
        if c[i]:
            for j in range(i*2, n+1, i):
                c[j] = False
    return c

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
p_list = prime_check(n)
sum = 0
first = 0
for i in range(m,n+1):
    if p_list[i] :
        sum +=i
        if first == 0:
            first = i
if sum == 0:
    print(-1)
else:
    print(sum)
    print(first)