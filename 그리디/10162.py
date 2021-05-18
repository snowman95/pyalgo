import sys
n = int(sys.stdin.readline())
button = (300,60,10)
cnt = [0,0,0]
for i in range(3):
    if n >= button[i]:
        mod = n//button[i]
        cnt[i] += mod
        n-= mod*button[i]
if n>0: 
    print(-1)
else :
    for i in cnt:
        sys.stdout.write(str(i) +' ')