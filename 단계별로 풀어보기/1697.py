import sys
import collections
n,k = map(int, sys.stdin.readline().split())
min_time = int(1e9)
def bfs(pos, time):
    global min_time
    q = collections.deque([(pos,0)])
    time[pos]= 0
    while q:
        cur = q.popleft()
        if cur[0]==k:
            min_time = min(min_time, cur[1])
            return
        for i in range(3):
            if i == 0:
                pos = cur[0]+1
            elif i == 1:
                pos = cur[0]-1
            else :
                pos = cur[0]*2
            if 0<=pos<=100000 :
                if time[pos] > pos:
                    time[pos] = pos
                    q.append((pos, cur[1]+1))
bfs(n, [int(1e9)]*100001)
print(min_time)