'''
좋은 단어

보고서의 모든 글자가 A와 B로 바뀌었다.
배열 위로 아치형 곡선 그었을때
-----
A   A

만약 선끼리 교차하지 않고 A-A, B-B를 짝 지을 수 있다면 좋은단어임.
이 좋은단어 개수를 세자.

[아이디어]
딱 붙어있는 문자가 모두 없어질 때까지
붙은 문자를 제거, 그 개수만큼 count
 
어떻게 없앨 것인가?

'''
import sys

n = int(sys.stdin.readline())
arr = list(sys.stdin.readline().strip() for _ in range(n))
good_word = 0
for cur_arr in arr:
    if len(cur_arr)%2 ==1:
        continue
    stack = []
    for s in cur_arr:
        if stack == [] or stack[-1] != s:
            stack.append(s)
        else:
            stack.pop()
    if stack == []: good_word+=1
print(good_word)