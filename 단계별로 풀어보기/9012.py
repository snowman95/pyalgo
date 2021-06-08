import sys
n = int(sys.stdin.readline())
for i in range(n):
    stack = sys.stdin.readline().rstrip()
    l = 0
    r = 0
    valid = 'YES'
    pre = stack[-1]
    if pre == ')': 
        r+=1
        for s in range(len(stack)-2, -1, -1):
            if stack[s] == '(': 
                if r > 0: r-=1
                else: 
                    valid = 'NO'
                    break
            else:
                if l > 0: l-=1
                else : r+=1
        if l>0 or r>0:
            valid = 'NO'
    else:
        valid = 'NO'
    print(valid)