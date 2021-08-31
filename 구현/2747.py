'''
피보나치 수

01
'''
import sys
n = int(sys.stdin.readline())
fibo = [0,1] + [0]*(n-1)
for i in range(2,n+1):
    fibo[i]=fibo[i-1]+fibo[i-2]
print(fibo[n])