'''
문자열 분석

문자열 N개
소문자, 대문자, 숫자, 공백의 개수 구하기
'''
import sys
for arr in sys.stdin:
    num, lower, upper, space = (0,0,0,0)
    for s in arr:
        s = ord(s)
        if 48 <= s <= 57 :  # 숫자
            num +=1
        elif 97 <= s <= 122 : # 소문자
            lower +=1
        elif 65 <= s <= 90 :  # 대문자
            upper +=1
        elif s == 32:
            space +=1
    print(lower, upper, num, space)