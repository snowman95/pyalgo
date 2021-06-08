# 중단... 
# 페르마소정리 쓰는거라는데 수학적인건 일단 넘어감.
    
# import sys
# n,k= map(int, sys.stdin.readline().split())
# dp = [[-1]*(n+1) for _ in range(n+1)]
# def func(n,k):
#     if dp[n][k] != -1:
#         return dp[n][k]
#     elif n==k or n==1:
#         dp[n][k] = 1
#     elif k==1:
#         dp[n][k] = n
#     else:
#         dp[n][k] = func(n-1,k-1) + func(n-1,k)
#     return dp[n][k] %1000000007
# if k == 0:
#     print(0)
# else:
#     print(func(n,k))
