import sys

max_value = -int(1e10)
min_value = -max_value
n = int(sys.stdin.readline())
num_arr = list(map(int, sys.stdin.readline().rstrip().split()))
oper_arr = ['+','-','*','/']
oper_cnt_arr = list(map(int, sys.stdin.readline().split()))
for i in range(4):
    oper_arr[i] *= oper_cnt_arr[i]

oper_str = ''.join(oper_arr)
oper_len = len(oper_str)

visit = [False]*oper_len
def dfs(cnt, arr):
    global max_value
    global min_value
    if cnt == oper_len:
        tmp = num_arr[0]
        for i in range(0,n-1):
            o = oper_str[arr[i]]
            if o == '+':
                tmp += num_arr[i+1]
            elif o == '-':
                tmp -= num_arr[i+1]
            elif o == '*':
                tmp *= num_arr[i+1]
            elif o == '/':
                if tmp >= 0:
                    tmp //= num_arr[i+1]
                else:
                    tmp = -tmp
                    tmp //= num_arr[i+1]
                    tmp = -tmp
        max_value = max(max_value, int(tmp))
        min_value = min(min_value, int(tmp))
        return
    for i in range(oper_len):
        if visit[i] == False:
            visit[i] = True
            arr.append(i)
            dfs(cnt+1, arr)
            visit[i] = False
            arr.pop()
    return

dfs(0,[])
print(max_value, min_value, sep='\n')

'''
n = int(sys.stdin.readline())
num_arr = list(sys.stdin.readline().rstrip().split())
oper_arr = ['+','-','*','/']
oper_cnt_arr = list(map(int, sys.stdin.readline().split()))
for i in range(4):
    oper_arr[i] *= oper_cnt_arr[i]
max_value = -int(1e10)
min_value = -max_value
for oper in list(itertools.permutations(''.join(oper_arr))):
    tmp = num_arr[0]
    for i in range(0,n-1):
        tmp = str(int(eval(tmp + oper[i] + num_arr[i+1])))
    max_value = max(max_value, int(tmp))
    min_value = min(min_value, int(tmp))
print(max_value, min_value, sep='\n')
'''