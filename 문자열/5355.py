'''
화성 수학

@는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자

숫자 + @%# 계산해라
'''
import sys, math
T = int(sys.stdin.readline())
for t in range(T):
    s = list(sys.stdin.readline().split())
    num = float(s[0])
    for i in range(1,len(s)):
        if s[i] == "@": num*=3
        elif s[i] == "%": num+=5
        else: num-=7
    print(f'{num:.2f}')
