import sys

'''
(~10만) N개의 회의. (시작,끝) 시간.
회의 끝나면 바로 시작가능. 이전 회의 끝시간 = 다음 회의 시작시간

끝시간을 오름차순 정렬하고 
'''
n = int(sys.stdin.readline())
arr = [tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]
arr.sort(key=lambda x : (x[1], x[0]))

cnt = 1
cur_time = arr[0][1]
for i in range(1,n):
    if arr[i][0] >= cur_time:
        cur_time = arr[i][1]
        cnt+=1
print(cnt)
