'''
스네이크버드

과일 먹으면 길이 1 늘어남.
i번째 과일의 높이는 hi

스네이크버는 자신의 길이 >= 과일높이hi 인 것을 먹을 수있다.
처음길이 L일때 과일먹어 늘릴 수 있는 최대 길이 구하라

과일 N개 (1~1000)
처음 길이 L (1~10000)
높이 hi (1~10000)

[아이디어]
정렬하고 최대한 많이먹어치우면 됨
'''
import sys
n,l = map(int, sys.stdin.readline().split())
height = sorted(list(map(int,sys.stdin.readline().split())))
for h in height:
    if l >= h: l+=1
    else: break
print(l)