'''
키 순서

1~N번 붙은 N명 학생 (모두 키 다름)

키가 작은 학생부터 자기가 몇 번째인지 알 수 있는 학생의 수

[아이디어]
정말 쉽게 푸는 방법은
1~n 까지 차례로 시작하며

매 순간 이동경로를 배열로 유지하고
가면서 만나는 애들한테 집합형태로 집어넣어
그리고 내차례일땐 내가 가는 경로를 나한테 집합으로 넣어버려
마지막 총 결산때 모든 배열로 갈 수 있으면 +1
'''
import sys, collections
n,m = map(int,sys.stdin.readline().split())
student = [[] for _ in range(n+1)]
relation = [0] *(n+1)
re_student = [[] for _ in range(n+1)]
re_relation = [0] *(n+1)
ans = 0

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    student[a].append(b)
    re_student[b].append(a)

for start in range(1,n+1):
    q = collections.deque([start])
    visited = [False]*(n+1)
    while q:
        cur = q.popleft()
        for next in student[cur]:
            if not visited[next]:
                visited[next]=True
                relation[next] +=1
                q.append(next)
    q = collections.deque([start])
    visited = [False]*(n+1)
    while q:
        cur = q.popleft()
        for next in re_student[cur]:
            if not visited[next]:
                visited[next]=True
                re_relation[next] +=1
                q.append(next)
for i in range(1,n+1):
    if relation[i]+re_relation[i] == n-1:
        ans+=1
print(ans)