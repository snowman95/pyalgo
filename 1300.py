# import sys
# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# inc_arr = [arr[0]] + [0]*n
# inc_idx = 0
# def binary_search(start, end, target):
#     global inc_arr
#     while start<=end:
#         mid = (start+end)//2
#         if inc_arr[mid] < target:
#             start = mid+1
#         elif inc_arr[mid] > target:
#             end = mid-1
#         else:
#             return -1
#     return end

# for i in range(1,n):
#     if inc_arr[inc_idx] < arr[i]:
#         inc_idx +=1
#         inc_arr[inc_idx]=arr[i]
#     else:
#         idx = binary_search(0,inc_idx, arr[i])
#         if idx != -1:
#             inc_arr[idx] = arr[i]
#             print(idx, arr[i],inc_arr)

# print(inc_arr)
# print(inc_idx+1)

import sys, bisect
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
inc_arr = [int(1e9)]*n

for i in range(0,n):
    idx = bisect.bisect_left(inc_arr, arr[i])
    if idx < n:
        inc_arr[idx] = arr[i]

print(bisect.bisect_left(inc_arr, int(1e9)))