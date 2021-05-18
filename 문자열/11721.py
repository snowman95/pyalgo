import sys
s = sys.stdin.readline().rstrip()
cnt = 0
for i in s:
    cnt+=1
    sys.stdout.write(i)
    if cnt%10 == 0:
        sys.stdout.write("\n")