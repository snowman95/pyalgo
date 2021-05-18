import sys
n = int(sys.stdin.readline())
cnt = 0
while n:
    last_five = n%5
    if last_five == 0:
        cnt += n//5
        break
    else:
        n-=3
        cnt+=1
if n<0: cnt = -1
print(cnt)