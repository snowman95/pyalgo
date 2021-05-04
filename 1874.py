import sys
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
ans = []
def push_pop():
    global ans
    next_num = 1
    stack = []
    for cur in arr:
        find_equal = False
        while stack:
            if stack[-1] < cur :
                break
            ans.append('-')
            if stack.pop() == cur:
                find_equal = True
                break
        if not find_equal:
            if cur < next_num:
                return False 
            d = cur-next_num+1
            for i in range(d):
                ans.append('+')
            ans.append('-')
            for i in range(next_num, cur):
                stack.append(i)
            next_num += d
    return True
if not push_pop():
    print('NO')
else :
    for i in ans:
        print(i)