import sys
n,m = map(int,sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(n)]
house.sort()
start = 1
end = house[-1]-house[0]
while start<=end:
    mid = (start+end)//2
    cur_house = house[0]
    cnt = 1
    for i in range(1, n):
        if cur_house + mid <= house[i]:
            cnt += 1
            cur_house = house[i]
    if cnt >= m:
        ans = mid
        start = mid+1
    else:
        end = mid-1

print(ans)