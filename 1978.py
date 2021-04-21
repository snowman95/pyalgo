'''
import sys
import math

def prime_check(n):
    if n == 1 :
        return False
    for div in range(2,int(math.sqrt(n))+1):
        if n%div == 0:
            return False
    return True

n = int(sys.stdin.readline())
numbers = map(int, sys.stdin.readline().split())
sum = 0
for number in numbers:
    if prime_check(number):
        sum+=1
print(sum)
'''

import sys
def prime_check(n):
    c = [False,False] + [True]*(n-1)
    for i in range(2, n+1):
        if c[i] == True:
            for j in range(2*i, n+1, i):
                c[j] = False
    return c
n = int(sys.stdin.readline())
numbers = map(int, sys.stdin.readline().split())
sum = 0
prime_list = prime_check(1000)
for number in numbers:
    if prime_list[number]:
        sum+=1
print(sum)
'''
n = int(sys.stdin.readline())
numbers = map(int, sys.stdin.readline().split())
prime = n
for number in numbers:
        for div in range(2,int(math.sqrt(number))+1):
            if number%div == 0:
                prime-=1
                break
print(prime)
'''