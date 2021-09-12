'''
최소 공통 조상 (LCA)

트리를 거슬러올라가면서 A,B가 공통으로 가지는 조상 노드 찾는것

각 노드의 부모노드들을 모두 저장한뒤 루트노드부터 차례대로 내려오며 
비교하여 같지 않은 노드가 나올때까지 반복한다. 
처음으로 같지않은 노드가 나왔을때 그 노드의 부모가 최소공통조상이라고 볼 수 있다.
'''

import sys
T=int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    # 각 노드의 부모노드 0으로 초기화
    p_list=[0 for _ in range(n+1)] 

    # 입력 : c의 부모는 p다 이렇게 들어오는 경우
    for _ in range(n-1):
        p,c = map(int,sys.stdin.readline().split())
        p_list[c] = p # 부모 노드 저장
 
    # 대상 a, b의 부모를 자기자신으로 설정
    a, b = map(int,sys.stdin.readline().split())
    a_parent = [a]
    b_parent = [b]

    #각 노드의 부모노드가 루트일때까지 모두 저장
    while p_list[a]:
        a_parent.append(p_list[a])
        a=p_list[a]
 
    while p_list[b]:
        b_parent.append(p_list[b])
        b=p_list[b]
 
    #같은 레벨로 맞추고 부모노드 같은거 찾기
    a_level=len(a_parent)-1
    b_level=len(b_parent)-1

    # 루트노드부터 부모노드가 같지 않을때까지 차례대로 비교
    while a_parent[a_level]==b_parent[b_level]:
        a_level-=1
        b_level-=1
 
    print(a_parent[a_level+1])


'''
더 빠르게 구해야 하는 경우

각 노드의 2^k번째의 부모노드를 dp[i][k]에 저장
두 노드의 레벨을 맞춘 뒤 최소공통조상을 구하면 된다.
레벨을 맞출때는 희소테이블과 비트연산의 and를 통해 찾아간다.

https://www.acmicpc.net/problem/11438
'''
import sys, math
from collections import deque
 
n = int(sys.stdin.readline())
logN = int(math.log2(n)+1)
tree = [[] for _ in range(n+1)] # 각 노드의 부모노드 저장
for _ in range(n-1):
    p, c= map(int,sys.stdin.readline().split())
    tree[c].append(p)
    tree[p].append(c)
 
p_list=[0 for _ in range(n+1)] # 부모노드 저장
depth=[0 for _ in range(n+1)] # 부모노드 개수
 
p_check=[True for _ in range(n+1)] #DFS를 위해 사용

#dfs로 모든 노드의 부모노드 찾기
q = deque()
q.append(1)
while q:
    p=q.popleft()
    p_check[p]=False
    for i in tree[p]:
        if p_check[i]:
            q.append(i)
            p_list[i] = p
            depth[i] = depth[p]+1 #깊이도 같이 저장해준다.

 
# 2^k번째 부모노드 저장
# log2 1000000=16.6096...
DP=[[0 for _ in range(logN)] for i in range(n+1)]
# 초기화
for i in range(n+1):
    DP[i][0]=p_list[i]
 
for j in range(1,logN):
    for i in range(1,n+1):
        # if DP[DP[i][j-1]][j-1]!=0:
            DP[i][j]=DP[DP[i][j-1]][j-1]
 
M=int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if depth[a]>depth[b]:
        a,b=b,a

    # 둘의 차이를 구하여 레벨 맞춰주기
    dif=depth[b]-depth[a]

    # b의 dif조상 찾기
    for i in range(logN):
        if dif & 1<<i: # ex dif의 11번째 부모노드를 구할 경우 경우 dif = 1011(2) b=DP[DP[DP[b][0]][1]][3]
            b=DP[b][i]
 
    if a==b:
        print(a)
        continue
 
    for i in range(logN-1,-1,-1):
        if DP[a][i]!=DP[b][i]:#처음으로 같지않은 부분으로가 가서 다시 검색
            a=DP[a][i]
            b=DP[b][i]
 
    print(DP[b][0])