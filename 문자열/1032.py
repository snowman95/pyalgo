'''
명령 프롬프트
패턴 검색
같은 길이의 알파벳과 .으로만 이루어진 문자열들을
?를 최대한 적게 사용해서 찾을 수 있는 패턴 출력

모든 문자열을 동시에 한글자씩 비교해서 하나라도 다르면 ? 박아
'''
import sys;
n = int(sys.stdin.readline())
arr = [ sys.stdin.readline().rstrip() for i in range(n)]
len = len(arr[0])
result = []
for idx in range(len):
    equal = True
    first_char = arr[0][idx]
    for item in range(1, n):
        if first_char != arr[item][idx]:
            equal = False
            break
    if equal:
        result.append(first_char)
    else:
        result.append('?')
        
for i in result:
    sys.stdout.write(i)