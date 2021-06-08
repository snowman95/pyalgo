import sys
arr = sys.stdin.readline().rstrip()
cnt = [0,0]
pre = arr[0]
for i in range(1,len(arr)):
    if pre != arr[i]:
        cnt[int(pre)] +=1
        pre = arr[i]
cnt[int(pre)] +=1
print(min(cnt))