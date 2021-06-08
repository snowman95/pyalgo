import sys
a,b = map(int,sys.stdin.readline().split())
cnt = 0
while a != b and a<b:
    cnt+=1
    str_b = str(b)
    if str_b[-1] == '1':
        str_b = str_b[:-1]
        if str_b : b = int(str_b)
        else: break
    else:
        if b%2 == 1:
            break
        b//=2
if a!=b:
    print(-1)
else : 
    print(cnt+1)