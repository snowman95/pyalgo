import sys
import math
'''
분해합 256(245+2+4+5)
10+1+0 = 11
11+1+1 = 13
'''
n = int(sys.stdin.readline())
if n < 10:
    print(0)
else :
    ans = math.inf
    for i in range(10,n+1):
        if (i + sum(map(int,list(str(i))))) == n:
            ans = i
            break
    if math.isinf(ans):
        print(0)
    else :
        print(ans)