'''
투 포인터
리스트에 순차적으로 접근해야할 때 
두개의 포인터를 이용하여 합을 구하는 기법
O(N)으로 해결가능

1) a+b = k
시작점 : 첫번째 원소
끝점 : 마지막 원소를 가리킨 상태에서 시작.
※ 정렬된 상태에서 진행이 필요하다.
'''
n = 1 # 수열 크기
arr = [] # 수열
x = 1 # a+b=x가 되는 그 x

arr.sort()
start, end, result = 1, n-1, 0
while start < end:
    total = arr[start] + arr[end]
    if total > x:
        end-=1
    elif total < x:
        start+=1
    else:
        start+=1
        result+=1

'''
2) 연속된 여러 숫자의 합 = k
시작점/끝점 : 첫번째 원소 가리킨 상태에서 시작.
'''
n = 1 # 수열 개수
s = 1 # 이 숫자를 만들어야 함
start, end, total_sum, result = 0, 0, 0, 0
for start in range(n):
    while total_sum < s and end < n:
        total_sum += arr[end]
        end +=1
    if total_sum == s:
        result +=1
    total_sum -=arr[start]

'''
3) 연속된 
연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중에 
가장 짧은 것의 길이구하기
'''
import sys
# n : 수열개수
# s : 이 숫자보다 큰 부분합 구해야함
n,s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
MAX = int(1e10)

start, end, total_sum, min_len = 0,0,0,MAX
for start in range(n):
    while total_sum < s and end < n:
        total_sum += arr[end]
        end+=1
    if total_sum >= s:
        min_len = min(min_len, end-start)
        total_sum -= arr[start]

if min_len == MAX:
    min_len = 0
print(min_len)


'''
4) 양/음수 섞인 수열
두 수의 합이 0에 가장 가까운 대상 2개
'''
import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()
start, end = 0,n-1
best = [int(1e10), 0,0]

while start < end:
    cur = abs(arr[start] + arr[end])
    if best[0] > cur:
        best = [cur, arr[start], arr[end]]
        
    next_end = abs(arr[start] + arr[end-1])
    next_start = abs(arr[start+1] + arr[end])
    if arr[start] + arr[end] == 0:
        break
    if next_start < next_end:
        start +=1
    elif next_start >= next_end:
        end-=1

print(best[1],best[2])