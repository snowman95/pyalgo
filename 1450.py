# import sys,bisect
# n,c = map(int,sys.stdin.readline().split())
# arr = list(map(int,sys.stdin.readline().split()))
# arr.sort()


# # 이분탐색 bisect
# # 이항계수 n까지 모두 구하기


# bin_arr = [[0]*(n) for _ in range(n)]
# bin_arr[0][0] = 1
# for i in range(1,n):
#     for j in range(i+1):
#         if j == 0 or j == n-1:
#             bin_arr[i][j] = 1
#         else:
#             bin_arr[i][j] = bin_arr[i-1][j-1]+bin_arr[i-1][j]

# cnt = 0
# right = bisect.bisect_right(arr, c)-1
# while right >=0:
#     last = c-arr[right]
#     if last >=0:
#         cnt += 1
#     if last > 0: # 용량이 남음
#         left = bisect.bisect_right(arr[0:right], last)-1
#         if arr[left] > last : # 담을거 없음
#             pass
#         else: # 0부터 left 위치까지를 담을 수 있음.
#             for i in range(left+1):
#                 cnt += bin_arr[left][i]
#     right-=1

# print(cnt+1)


import sys 
n, c = map(int, sys.stdin.readline().split()) 
weight = list(map(int, sys.stdin.readline().split())) 
aw = weight[:n // 2] 
bw = weight[n // 2:] 
asum = []
bsum = []

def bruteforce(arr, sumarr, l, w): 
    if l >= len(arr): 
        sumarr.append(w) 
        return 
    bruteforce(arr, sumarr, l + 1, w) 
    bruteforce(arr, sumarr, l + 1, w + arr[l]) 

def binarysearch(arr, target, start, end): 
    while start < end: 
        mid = (start + end) // 2 
        if arr[mid] <= target: 
            start = mid + 1 
        else: end = mid 
    return end 

bruteforce(aw, asum, 0, 0) 
bruteforce(bw, bsum, 0, 0) 
bsum.sort() 
cnt = 0 
for i in asum: 
    if i > c:
        continue 
    cnt += binarysearch(bsum, c-i, 0, len(bsum)) 
print(cnt)