'''
오르막 수

오름차순을 이루는 수
2234, 11119 = 오르막 수
2232 = 아님

길이가 N인 모든 오르막 수의 개수 구해라
0으로 시작하는 숫자도 존재! = 문자열로 풀어야함.

ex)
N=1 : 10
0~9
N=2 : 10+9+...+1 = 55
00~9 = 10
11~9 = 9
22~9 = 8
99~9 = 1
N=3 : 
000~9 = 10
011~9 = 9
099~9 = 1
→ 55개

111~9 = 9
129~9 = 8
199~9 = 1
→ 55-10 = 45개

999~9 = 1개

...
55+(55-10)+(55-10-9)+(55-10-9-8)+...+(55-10..-2)

N=4 :
0000~9, ..., 0999~9 = 위와 동일
1111~9
1199~9
1999~9
이건?
55를 뺀것

결론
[10,9,8,7,6,5,4,3,2,1]        = a[1]
[(10~1),(9~1),(8~1),...(1~1)] = a[1]*10 - a[1]
[(10~1+9~1+8~1+...+1~1),(9~1+8~1+...+1~1),...,(1~1)]

'''
import sys
n = int(sys.stdin.readline())
arr = [1]*10
for i in range(1,n):
    next_arr = [sum(arr)]
    for j in range(9):
        next_arr.append(next_arr[-1]-arr[j])
    arr = next_arr
print(sum(arr)%10007)