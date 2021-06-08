import sys
while(True):
    stack = sys.stdin.readline().rstrip()
    trash = []
    valid = 'yes'
    if stack == '.':
        break
    for i in range(len(stack)-1, -1, -1):
        s = stack[i]
        if s == ')' or s == ']':
            trash.append(s)
        elif s == '(' or s == '[':
            if not trash:
                valid = 'no'
                break
            t = trash.pop()
            if s =='(':
                if t == ']':
                    valid = 'no'
                    break
            elif s == '[' :
                if t == ')':
                    valid = 'no'
                    break
    if trash:
        valid = 'no'
    print(valid)