import string

string.digits # 0~9
string.ascii_lowercase # a~z
string.ascii_uppercase # A~Z
string.ascii_letters # a~zA~Z

# 대소문자 변환
str().lower() # 전체문자열 소문자 변환
str().upper() # 전체문자열 대문자 변환

# 치환
str().replace('바꿀대상','바꿀값')
while '바꿀대상' in str():
    str() = str().replace('바꿀대상','바꿀값')

# 아스키 코드  변환
ord('a') # ord(str()) → 아스키코드(숫자)로 변환
chr(1) # 아스키코드(숫자) → 문자로 변환


# ['a','b','c'] → 'abc'
''.join(['a','b','c'])

# [1,2,3] → '123'
''.join(map(int, [1,2,3]))