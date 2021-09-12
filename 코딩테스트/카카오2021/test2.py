'''
양의 정수 n이 주어집니다. 
이 숫자를 k진수로 바꿨을 때, 
변환된 수 안에 아래 조건에 맞는 소수(Prime number)가 몇 개인지 알아보려 합니다.

0P0처럼 소수 양 쪽에 0이 있는 경우
P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
P처럼 소수 양쪽에 아무것도 없는 경우

단, P는 각 자릿수에 0을 포함하지 않는 소수입니다.
예를 들어, 101은 P가 될 수 없습니다.
예를 들어, 437674을 3진수로 바꾸면 211020 101 011입니다. 
여기서 찾을 수 있는 조건에 맞는 소수는 왼쪽부터 순서대로 211, 2, 11이 있으며, 총 3개입니다. 
211은 P0 형태에서 찾을 수 있으며, 
2는 0P0에서, 
11은 0P에서 찾을 수 있습니다.

정수 n과 k가 매개변수로 주어집니다. n을 k진수로 바꿨을 때, 변환된 수 안에서 찾을 수 있는 위 조건에 맞는 소수의 개수를 return 하도록 solution 함수를 완성해 주세요.




'''
import math, string, sys
sys.setrecursionlimit(10000)
def prime_check(n):
    if n == 1 :
        return False
    for div in range(2,int(math.sqrt(n))+1):
        if n%div == 0:
            return False
    return True

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def to_radix(n, b):
    """10진수를 n진수로 변환하기"""
    if n < b:
        return str(n)
    s = to_radix(n//b, b)
    return s + str(n%b)
    
def solution(n, k):
    answer = 0
    if k != 10:
        num = str(convert(n, k)) # k 진수변환
    else:
        num = str(n)
    size = len(num)
    for i in range(size):
        for j in range(i, size):
            s = num[i:j+1] # i~j 까지를 뽑아서 확인
            if '0' in s:
                continue
            if prime_check(int(s)):
                # 0P 확인
                if i != 0 and j == size-1 and num[i-1]=='0':
                    answer +=1
                # P0 확인
                elif i == 0 and j != size-1 and num[j+1]=='0': 
                    answer +=1
                # 0P0 확인
                else:
                    if i != 0 and j != size-1 and num[i-1]=='0'and num[j+1]=='0': 
                        answer +=1
    # p 확인
    if prime_check(int(num)) and '0' not in num  : 
        answer +=1
    return answer

n = 437674
k = 3
solution(n,k)