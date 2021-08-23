'''
KMP는 왜 KMP일까?
맨 앞글자와 -뒤의 대문자를 연결

-를 찾아야하나?
아니면 대문자만

'''
import sys
s = sys.stdin.readline().strip()
for i in s:
    if 65<=ord(i)<=90:
        sys.stdout.write(i)