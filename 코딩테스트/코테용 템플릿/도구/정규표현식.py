'''
정규표현식 시각화
https://regexr.com/
'''

import re
'''
[abc]    : [] 사이의 문자들과 매치
[a-b]    : 하이픈(-) 추가하면 두 문자 사이 범위를 의미
[a-zA-Z] : 알파벳
[0-9]    : 숫자
[^0-9]   : 숫자가 아닌 것 (맨앞에 ^를 붙이면 not의 의미)

대문자는 소문자의 반대(^)의 의미라고 기억
\d : 숫자와 매치, [0-9] 와 동일
\D : 숫자 아닌 것과 매치, [^0-9] 와 동일
\s : whitespace 문자와 매치, [ \t\n\r\f\v] 와 동일. 맨앞 빈칸은 공백문자를 의미함.
\S : whitespace 문자 아닌 것과 매치, [^ \t\n\r\f\v]와 동일.
\w : 문자+숫자와 매치, [a-zA-Z0-9] 와 동일
\W : 문자+숫자 아닌 것과 매치, [^a-zA-Z0-9] 와 동일
Dot .	줄바꿈 문자 \n 제외한 모든 문자와 매치 (문자 .을 쓰고싶다면 a[.]b)


a.b = a+모든문자+b

반복 * : *앞에 있는 문자가 0회 이상 반복가능 (하나도 없어도 됨 : a가 하나도 없는 ct도 가능)
ca*t : ct, cat, caat, caaa…t

반복 + : +앞에 있는 문자가 1회 이상 반복가능
ca+t : cat, caat, caaa…t

반복 {m,n} : 반복 횟수를 제한하고 싶은 경우 m부터 n까지 매치가능, m또는 n 생략 가능
{m} : m회 이상, {,n} : n회 이하

반복 ? : {0,1} 을 의미한다. 즉, 문자 0~1개 (있거나 없거나)


\	\은 \\로 써줘야 문자로 인식함.  
\\은 \\\\로 써줘야 문자로 인식함. 
혹은 정규식 문자열 앞에 r 문자를 삽입해도 됨 (Raw String) = 입력한 문자 그대로 인식
p = re.compile(r'\\section')
'''

regex = '[a-z]+'
# re.compile : 한 객체를 여러 번 사용할때 쓴다.
p = re.compile(regex)

m = p.match("python") 
m.group()	# 매치된 문자열을 돌려준다.
m.start()	# 매치된 문자열의 시작 위치를 돌려준다.
m.end()	    # 매치된 문자열의 끝 위치를 돌려준다.
m.span()	# 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.

p = re.compile('정규표현식', re.DOTALL)
p = re.compile('정규표현식', re.IGNORECASE)
p = re.compile('정규표현식', re.MULTILINE)
p = re.compile('정규표현식', re.VERBOSE)
'''
옵션
DOTALL(S)	  Dot이 줄바꿈 문자('\n')를 포함하여 모든 문자와 매치할 수 있도록 한다.
IGNORECASE(I) 대소문자에 관계없이 매치할 수 있도록 한다.
MULTILINE(M)  여러줄과 매치할 수 있도록 한다. 
VERBOSE(X)    verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)
'''
