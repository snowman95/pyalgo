import sys
seq = 0
while True:
    l,p,v = map(int,sys.stdin.readline().split())
    if l==0 and p==0 and v==0:
        break
    a = v//p
    b = v%p
    seq +=1
    if b != 0:
        if l < b:
            b = l
    print(f"Case {seq}: {a*l+b}")