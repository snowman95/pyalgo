import sys
n,m = map(int, sys.stdin.readline().split())
arr1 = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

m,k = map(int, sys.stdin.readline().split())
arr2 = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

ans_arr = [[0]*k for _ in range(n)]
for x in range(n):
    for y in range(k):
        for z in range(m):
            ans_arr[x][y]+=arr1[x][z]*arr2[z][y]

for i in range(n):
    for j in range(k):
        sys.stdout.write(str(ans_arr[i][j]) +' ')
    sys.stdout.write('\n')