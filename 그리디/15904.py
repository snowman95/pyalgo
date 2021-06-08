import sys
arr = sys.stdin.readline().rstrip()
upcp = "UCPC"
idx = 0
for a in arr:
    if upcp[idx] == a:
        idx+=1
        if idx==4:
            break

if idx==4:
    print('I love UCPC')
else:
    print('I hate UCPC')