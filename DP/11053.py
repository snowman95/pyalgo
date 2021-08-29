'''
가장 긴 증가하는 부분 수열
'''
import sys, bisect
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
lsi_arr = [sys.maxsize]*n
idx_arr = [0]*n

for i,cur in enumerate(arr):
    insert_pos = bisect.bisect_left(lsi_arr, cur)
    lsi_arr[insert_pos] = cur
    idx_arr[i] = insert_pos

lsi_length = bisect.bisect_left(lsi_arr, sys.maxsize)
print(idx_arr)
# lsi의 요소 출력하기
result = []
end = max(idx_arr)
for i in range(n-1,-1,-1):
    if idx_arr[i]== end:
        result.append(arr[i])
        end-=1
result.reverse()
for i in result:
    print(i, end=" ")