import sys
T = int(sys.stdin.readline())
for t in range(T):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    sort_arr = []
    for i in range(n):
        sort_arr.append((arr[i],i))
    sort_arr.sort()
    ans = 0
    visited = [False]*n
    for i in range(n-1,-1,-1):
        for j in range(sort_arr[i][1]-1,-1,-1):
            if visited[j] :
                break
            ans += sort_arr[i][0] - sort_arr[j][0]
            visited[j]=True
            
    print(ans)