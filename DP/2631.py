'''
줄세우기

1~N번 번호 붙은 N명의 아이들
오름차순으로 줄 세운다. 한번에 1명 옮길 수 있다.
오름차순 정렬할때의 최소 횟수 구해라

3 7 5 2 6 1 4
아이들을 순서대로 줄을 세우기 위해, 먼저 4번 아이를 7번 아이의 뒤로 옮겨보자. 그러면 다음과 같은 순서가 된다.
3 7 4 5 2 6 1
이제, 7번 아이를 맨 뒤로 옮긴다.
3 4 5 2 6 1 7
다음 1번 아이를 맨 앞으로 옮긴다.
1 3 4 5 2 6 7
마지막으로 2번 아이를 1번 아이의 뒤로 옮기면 번호 순서대로 배치된다.
1 2 3 4 5 6 7

[아이디어]
가장 긴 증가하는 부분수열 LIS를 찾고 나머지 부분을 이동시키면 된다.

3 5 6 4 이런 경우에 3과 5 사이에 4를 끼워서 3 4 5 6이 되는데
3 5 6 이 증가하는 부분 수열 중 가장 크다는 걸 알 수 있다.

'''
import sys, bisect
n = int(sys.stdin.readline())
idx_arr = [0]*n
arr = list(map(int, sys.stdin.readline().split()))
inc_arr = [sys.maxsize]*n

for i in range(0,n):
    idx = bisect.bisect_left(inc_arr, arr[i])
    inc_arr[idx] = arr[i]
    idx_arr[i]=idx
print(bisect.bisect_left(inc_arr, sys.maxsize))

result = []
end = max(idx_arr)
size = len(idx_arr)
for i in range(size-1,-1,-1):
    if idx_arr[i]== end:
        result.append(arr[i])
        end-=1
result.reverse()
for i in result:
    print(i, end=" ")