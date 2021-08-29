'''
2+1 세일

한번에 제품 3개사면 가장 싼 것은 무료로 준다.
나머지 2개 값만 지불

7개의 유제품이 있어서 각 제품의 가격
10, 9, 4, 2, 6, 4, 3
재현이가 (10, 3, 2), (4, 6, 4), (9)로 총 3번 구매
첫 번째 꾸러미에서는 13원을, 
두 번째 꾸러미에서는 10원을, 
세 번째 꾸러미에서는 9원을 지불해야 합니다.

총 N개 사려고할때의 최소비용 구해라

[아이디어]
내림차순 정렬 후 앞에서 부터 3개씩 끊어버리면 됨
'''
import sys
n = int(sys.stdin.readline())
arr = sorted(list(int(sys.stdin.readline()) for _ in range(n)),reverse=True)
cnt = 0
add = 0
total = 0
for i in range(n):
    cnt+=1
    if cnt == 3:
        total += add
        add = 0
        cnt = 0
    else:
        add += arr[i]
total += add
print(total)