import sys
x = int(sys.stdin.readline())
dx=(0,1,1,-1)
dy=(1,-1,0,1)
up,down = 1,1
state = 0
while x!=1:
    up += dx[state]
    down += dy[state]
    if state == 0 or state ==2:
        state +=1
    elif state == 1:
        if down == 1:
            state +=1
    elif state == 3:
        if up == 1:
            state =0
    x-=1
print(f"{up}/{down}")