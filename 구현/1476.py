'''
날짜 계산

수 3개를 이용해 연도 나타냄 
E 지구 (1~15)
S 태양 (1~28)
M 달   (1~19)

우리의 1년 = 1 1 1
1년 지나면 = 2 2 2
15        = 15 15 15
16        = 1  16 16 (E의 범위를 벗어나 1로 리셋됨)

ESM이 주어졌을때 우리의 연도로 변환해라

내 생각엔 특정 수가 나올때까지 줄줄이 증가?
1 1 1 부터 무지성 증가 
'''
import sys
cnt = 1
e,s,m = [1,1,1]
re,rs,rm = map(int, sys.stdin.readline().split())
while (re != e) or (rs != s) or (rm != m):
    if e==15: e=1
    else : e+=1

    if s==28: s=1
    else : s+=1

    if m==19: m=1
    else : m+=1
    cnt+=1
print(cnt)