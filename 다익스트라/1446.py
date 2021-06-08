import sys
n,d = map(int,sys.stdin.readline().split())
board = [[] for _ in range(10001)]
for _ in range(n):
    x,y,dist = map(int,sys.stdin.readline().split())
    board[x].append((y,dist))

dist_arr = [i for i in range(d+1)]
for i in range(d+1):
    if i != 0:
        dist_arr[i]=min(dist_arr[i], dist_arr[i-1]+1)
    for e,dist in board[i]:
        if e <=d and dist_arr[e] > dist + dist_arr[i]:
            dist_arr[e] = dist+dist_arr[i]
print(dist_arr[d])