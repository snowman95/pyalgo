import sys
n = int(sys.stdin.readline())
arr = sys.stdin.readline().rstrip()

man, lcount = 0, 0
block = False

for i in range(n):
    if arr[i]=='L':
        if lcount == 0:
            if block:
                lcount +=1
            else:
                lcount +=1
                block = True
                man+=1
        elif lcount == 1:
            man += 1
            lcount = 0
            block = True
    else:
        man+=1
print(man)