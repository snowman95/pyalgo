import sys
arr = [0,1,1,1,2,2] + [0] *100

for a in range(6,101):
    arr[a] = arr[a-5]+arr[a-1]

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    print(arr[n])