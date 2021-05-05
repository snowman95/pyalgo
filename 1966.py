import sys, collections

T = int(sys.stdin.readline())
for t in range(T):
    n, m = map(int, sys.stdin.readline().split())
    weight = list(zip(map(int, sys.stdin.readline().split()) , range(0,n)))
    q = collections.deque(weight)
    sort_weight = sorted(weight, reverse=True)
    for i in range(n):
        item = (0,0)
        while True:
            item = q.popleft()
            if sort_weight[i][0] != item[0]:
                q.append(item)
            else:
                break
        if m == item[1]:
            print(i+1)
            break