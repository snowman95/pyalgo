import sys
T = int(sys.stdin.readline())
types =(25,10,5,1)
for t in range(T):
    c = int(sys.stdin.readline()) * 100
    ans = [0,0,0,0]
    for i in range(4):
        if c >=types[i]:
            ans[i]=c//types[i]//100
            c -= types[i]*ans[i]*100
    print(*ans)