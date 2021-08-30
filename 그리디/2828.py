'''
사과 담기 게임

N칸으로 나뉘어진 스크린
스크린 아래쪽에는 M칸을 차지하는 바구니 있다. (M < M)
1234567 -> 스크린
___     -> 바구니
이런 느낌인데 N칸 중 한 칸에서 사과가 직선하강한다.
바닥에 닿으면 즉시 다른 사과가 떨어짐.
바구니가 사과가 떨어지는 칸 차지한다면, 사과 담을 수 있음.

모든 사과 담으려 할때 바구니의 최소 이동거리?

5 1
3
1
5
3
걍 무지성으로 순서대로 따라가면 되는 문제인것 같은데?
'''
import sys
n,m = map(int,sys.stdin.readline().split())
j = int(sys.stdin.readline())

s = 1
e = m
total_dist = 0
for i in range(j):
    pos = int(sys.stdin.readline())
    # 스크린 범위: 1~n
    dist = 0
    if pos < s : dist = pos-s
    elif e < pos: dist = pos-e
    s += dist
    e += dist
    total_dist += abs(dist)
print(total_dist)