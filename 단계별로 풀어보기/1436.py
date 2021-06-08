import sys
n = int(sys.stdin.readline())
last_num_list = ['666']
ans = []
def recur(cur_list,dep):
    global ans
    ans += cur_list
    if dep == 4:
        return 
    recur(append_num(cur_list), dep+1)

def append_num(input_list):
    new_list = []
    for i in input_list:
        for j in range(0,9+1):
            new_list.append(str(j)+i)
            new_list.append(i+str(j))
    return new_list

recur(last_num_list, 0)
a = list(set(map(int, ans)))
a.sort()
print(a[n-1])