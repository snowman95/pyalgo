import sys
n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))
array.sort()
[print(i) for i in array]