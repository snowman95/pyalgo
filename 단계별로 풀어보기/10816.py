import sys, bisect
n = int(sys.stdin.readline())
target = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
find_nums = map(int,sys.stdin.readline().split())

target.sort()

for i in find_nums:
    left = bisect.bisect_left(target,i)
    right = bisect.bisect_right(target,i)
    sys.stdout.write(str(right-left) + ' ')