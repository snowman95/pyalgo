'''
피보나치

ƒK는 ƒK = ƒK-1 + ƒK-2로 정의되며 
초기값은 ƒ0 = 0과 ƒ1 = 1
정수 100은 ƒ4 + ƒ6 + ƒ11 = 3 + 8 + 89 
또는 ƒ1 + ƒ3 + ƒ6 + ƒ11 = 1 + 2 + 8 + 89, 
또는 ƒ4 + ƒ6 + ƒ9 + ƒ10 = 3 + 8 + 34 + 55 
등으로 나타낼 수 있다. 

이 문제는 하나의 양의 정수를 
최소 개수의 서로 다른 피보나치 수들의 합으로 나타내는 것이다. 

[아이디어]
1. 피보나치 수를 미리 구해둔다.
만들값-현재값을 피보나치 배열에서 이분탐색으로 빠르게 찾는다.
못만들면 그 다음 차례로 넘어가는 방식.

'''
import sys, bisect
fibo = [1,2]
idx = 2
while fibo[-1] < 10e9:
    fibo.append(fibo[idx-1]+fibo[idx-2])
    idx+=1

T = int(sys.stdin.readline())
for t in range(T):
    goal = int(sys.stdin.readline())
    arr = []
    while goal > 0:
        idx = bisect.bisect_left(fibo, goal)
        if goal < fibo[idx]: idx-=1
        goal -= fibo[idx]
        arr.append(fibo[idx])
    print(*sorted(arr))