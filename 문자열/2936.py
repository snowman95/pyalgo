'''
소음

10의 제곱 형태
+ 또는 *
10의 제곱 형태
그것의 결과 구해라
'''
import sys
a = int(sys.stdin.readline())
oper = sys.stdin.readline().strip()
b = int(sys.stdin.readline())
if oper == "*": print(a*b)
else: print(a+b)