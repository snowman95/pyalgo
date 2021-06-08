import sys
T = int(sys.stdin.readline())
for t in range(T):
    k = int(sys.stdin.readline())
    page = list(map(int, sys.stdin.readline().split()))
    table = [[0]*k for _ in range(k)] 
    for i in range(k-1): 
        table[i][i+1] = page[i] + page[i+1] 
        for j in range(i+2, k): 
            table[i][j] = table[i][j-1] + page[j] 

    for d in range(2, k):
        for i in range(k-d): 
            j = i+d 
            minimum = [table[i][p] + table[p+1][j] for p in range(i, j)] 
            table[i][j] += min(minimum) 
    print(table[0][k-1])