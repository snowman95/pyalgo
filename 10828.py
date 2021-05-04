import sys
n = int(sys.stdin.readline())
stack = []
com_arr = [list(sys.stdin.readline().split()) for i in range(n)]
for com in com_arr:
    if com[0] == 'push':
        stack.append(int(com[1]))
    elif com[0] == 'pop':
        if stack : print(stack.pop())
        else: print(-1)
    elif com[0] == 'top':
        if stack : print(stack[-1])
        else: print(-1)
    elif com[0] == 'size':
        print(len(stack))
    elif com[0] == 'empty':
        if stack : print(0)
        else: print(1)