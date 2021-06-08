import sys
n = int(sys.stdin.readline())


def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n

print(factorial(n))

'''
import sys
import math
n = int(sys.stdin.readline())
print(math.factorial(n))
'''