'''
ROT13

"Baekjoon Online Judge"를 ROT13으로 암호화하면 "Onrxwbba Bayvar Whqtr"
ROT13는 알파벳 대/소문자만 적용 가능하다. 나머지는 그대로

Baekjoon Online Judge
Onrxwbba Bayvar Whqtr

[아이디어]
a 97 z 122
A 65 Z 90
'''
import sys
a = sys.stdin.readline()
for i in range(len(a)):
    s = ord(a[i])
    if 97<=s<=122: 
        s+=13
        if s > 122: s = s-122+96
    elif 65<=s<=90: 
        s+=13
        if s > 90: s = s-90+64
    sys.stdout.write(chr(s))