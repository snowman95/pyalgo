'''
소수 경로

- 입력 : 1000~9999 사이의 소수
- 로직 : A→B로 변환.
  - 한번에 1개의 숫자만 변경 가능하다. (맨앞자리 0불가)
  - 항상 소수를 유지해야함.
- 출력
  - 불가능하면 Impossible
  - 가능하면 변환에 필요한 최소 횟수

아이디어 메모
1. 사전에 1000~9999 사이의 모든 소수를 구한다.
prime_arr = []

2. A와 한글자만 다른 소수로 변경. 
- 변경가능시 사용된 소수는 visited=True, count+=1. B가 나오면 중단.
- 진행불가시 = Impossible

한글자만 다른 소수 판별방법?
for num in prime_arr:
    for i in range(4):
        num[i]==cur[i] 일케?

'''
import sys,math,collections
T = int(sys.stdin.readline())

min_cnt = 9999999999
visited = {}
def prime_check(n):
    if n == 1 :
        return False
    for div in range(2,int(math.sqrt(n))+1):
        if n%div == 0:
            return False
    return True

def bfs(start, end):
    global min_cnt
    q = collections.deque([(start,0)])
    visited[start] = True
    while q:
        cur,cnt = q.popleft()
        visited[cur] = True
        if cur == end:
            min_cnt = min(min_cnt, cnt)
            break
        for num in visited.keys():
            eqaul_cnt = 0
            for i in range(4):
                if num[i]==cur[i]: eqaul_cnt+=1
            if eqaul_cnt == 3 and not visited[num]:
                q.append((num,cnt+1))

for i in range(1000,10000):
    if prime_check(i):
        visited[str(i)]=False

for t in range(T):
    min_cnt = 9999999999
    a,b = sys.stdin.readline().rstrip().split()
    bfs(a,b)
    if min_cnt == 9999999999:
        print('Impossible')
    else:
        print(min_cnt)
    for key in visited:
        visited[key] = False