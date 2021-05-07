'''
import sys
n = int(sys.stdin.readline())
target = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
find_nums = map(int,sys.stdin.readline().split())

target.sort()
def binary_search(s,e,item):
    global target
    while s <= e:
        mid = (s+e)//2
        if target[mid] ==  item:
            return 1
        elif target[mid] > item:
            e = mid-1
        else:
            s = mid+1
    return 0

for i in find_nums:
    print(binary_search(0, n-1, i))


'''
import sys, bisect
n = int(sys.stdin.readline())
target = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
find_nums = map(int,sys.stdin.readline().split())

target.sort()

for i in find_nums:
    a = bisect.bisect_left(target,i)
    if a < n and i == target[a]:
        print(1)
    else:
        print(0)