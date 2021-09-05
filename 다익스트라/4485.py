'''
다익스트라

녹색 옷 입은 애가 젤다지?

NxN 크기 맵 (2~125)
각 칸에는 잃는 금액 있음(0~9)
인접 4방향 이동 가능
주인공 [0][0] 위치-> [N-1][N-1] 이동할때의 최소비용

'''
import sys, heapq
dx = (0,0,1,-1)
dy = (1,-1,0,0)
cnt = 1
while True:
    n = int(sys.stdin.readline())
    if n == 0: break
    board = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
    start = (0,0)
    INF = n*n*9+1
    dist_arr = [[INF] * n for _ in range(n)]
    dist_arr[0][0] = 0
    q = []
    heapq.heappush(q,(0, start))

    while q:
        dist, (x,y) = heapq.heappop(q)
        if dist_arr[x][y] < dist:
            continue
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<n:
                next_dist = dist + board[nx][ny]
                if dist_arr[nx][ny] > next_dist:
                    dist_arr[nx][ny] = next_dist
                    heapq.heappush(q,(next_dist, (nx,ny)))
    print(f'Problem {cnt}: {dist_arr[n-1][n-1]+ board[0][0]}')
    cnt+=1