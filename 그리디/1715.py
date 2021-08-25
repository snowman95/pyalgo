'''
카드 정렬하기

정렬된 두 묶음의 숫자 카드
각 묶음 카드수 A,B 를 하나로 합치려면 A+B번 비교
ex) 20장 + 30장 = 50번비교

이 카드묶음을 선택하는 순서에 따라 비교횟수 줄어들 수 있음
N개 숫자 카드의 크기 주어질때 최소 비교 횟수

1. 오름차순 정렬
2. 가장작은것 더한다.
3. 하나만 남을때까지 반복
'''
import sys, heapq
n = int(sys.stdin.readline())
heap = [int(sys.stdin.readline()) for _ in range(n)]
heapq.heapify(heap)
total = 0
idx = 0
while idx+1<n:
    add = heapq.heappop(heap)+heapq.heappop(heap)
    heapq.heappush(heap,add)
    total +=add
    idx+=1
print(total)