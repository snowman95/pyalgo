'''
거스름돈

동전 개수 최소가 되도록 2,5원으로만 거슬러줌.
거스름돈 = n일때
5를 최대한 많이
그다음에 2를 최대한 많이

5는 2의 배수는 아님
15 = 5*3
14 = 5*2+2*2
13 = 5*1+2*4

1. 2를 하나씩 빼다가 5로 나눠지면 끝내면 됨.
- 마지막에 1 또는 3이 남은경우
- 5로 나눠떨어지는 경우

'''
import sys
n = int(sys.stdin.readline())
cnt = 0
while n:
    if n==1 or n==3 or n%5==0:
        break
    n-=2
    cnt+=1
if n==0: print(cnt)
else:
    if n%5==0: print(cnt + n//5)
    else : print(-1)