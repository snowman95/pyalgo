import sys
k = int(sys.stdin.readline())

pre = [1,0]
next = [0,1]
for i in range(2,k+1):
    pre,next = next,pre
    next[0] += pre[0]
    next[1] += pre[1]

sys.stdout.write("%d %d" %(next[0],next[1]))