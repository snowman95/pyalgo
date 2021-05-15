import sys
T = int(sys.stdin.readline())
for t in range(T):
    n = int(sys.stdin.readline())
    items = {}
    ans = 1
    for i in range(n):
        name, types = sys.stdin.readline().rstrip().split()
        if types not in items:
            items[types] =2
        else:
            items[types] +=1
    for i in items.values():
        ans *= i
    print(ans-1)