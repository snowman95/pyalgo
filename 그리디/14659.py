'''
한조서열정리하고옴ㅋㅋ

N개의 산봉우리, 봉우리마다 활잡이 한명씩
자신보다 낮은 봉우리에 있는 적만 처치 가능

처음 출발한 봉우리보다 높은 봉우리 만나면 공격 포기
봉우리 높이는 모두 다르고 모든 용은 오른쪽으로 나아감.

[아이디어]
이중 for문
나보다 큰것 만날때까지 진행
'''
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
max_kill = 0
for i in range(n):
    kill = 0
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            kill+=1
        else:
            break
    max_kill = max(max_kill, kill)
print(max_kill)