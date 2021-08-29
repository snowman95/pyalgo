'''
숨바꼭질

헛간개수 N(2~20000)
1부터 센다.

모든 헛간은 M(1~50000)개의 양방향 길로 이어짐
양끝을 A_i 와 B_i 로 나타냄.
(1<= A_i <= N; 1 <= B_i <= N; A_i != B_i)

[입력]
첫 번째 줄에는 N과 M이 공백을 사이에 두고 주어진다.
이후 M줄에 걸쳐서 A_i와 B_i가 공백을 사이에 두고 주어진다.

[출력]
첫 번째는 숨어야 하는 헛간 번호를
(만약 거리가 같은 헛간이 여러개면 가장 작은 헛간 번호를 출력)
두 번째는 그 헛간까지의 거리를, 
세 번째는 그 헛간과 같은 거리를 갖는 헛간의 개수를 출력해야한다.

[아이디어]
1에서 최대한 많이 가면 됨.
'''
import sys, collections
n, m = map(int, sys.stdin.readline().split())
home = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    home[a].append(b)
    home[b].append(a)

visited = [0]*(n+1)
q = collections.deque([(1,0)])
visited[1] = 1

while q:
    cur, level = q.popleft()
    for next in home[cur]:
        if visited[next] == 0:
            visited[next] = level+1
            q.append((next,level+1))
visited[1] = 0
l = 0
ans = 1
for i in range(2,n+1):
    print(i)
    if visited[i] > l:
        ans = i
        l = visited[i]
print(ans, l, visited.count(l))