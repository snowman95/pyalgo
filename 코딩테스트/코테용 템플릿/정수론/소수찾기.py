'''
단발성
단순 소수 검사 함수
'''
import math
def prime_check(n):
    if n == 1 :
        return False
    for div in range(2,int(math.sqrt(n))+1):
        if n%div == 0:
            return False
    return True

'''
저장성
에라토스테네스의 체
메모리 써서 미리 소수여부를 확인하는 것
'''
def prime_check(n):
    c = [False,False] + [True]*(n-1)
    for i in range(2, n+1):
        if c[i] == True:
            for j in range(2*i, n+1, i):
                c[j] = False
    return c