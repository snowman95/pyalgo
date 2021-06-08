import sys
arr1 = ' ' + sys.stdin.readline().rstrip()
arr2 = ' ' + sys.stdin.readline().rstrip()

a_len = len(arr1)
b_len = len(arr2)
dp = [[0] * (b_len) for _ in range(a_len)]

for i in range(1, a_len):
    for j in range(1, b_len): 
        if arr1[i] == arr2[j]: 
            dp[i][j] = dp[i-1][j-1] + 1 
        else: 
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
print(dp[a_len-1][b_len-1])