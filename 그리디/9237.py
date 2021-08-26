'''
이장님 초대

묘목 N개
묘목 1개 심는데 1일, 다자라는데 ti일
모든 나무가 다자라면 이장님 초대 = 며칠 걸리는지 구하기

[아이디어]
자라는데 오래 걸리는 나무부터 심는다.

첫날에 묘목 사는데 1일 소요
day = 1
day += len(arr)
tree_arr.sort(reverse=True)
1 2 3 4 5 6 7 
  4 4 4 4 4
    3 3 3 3
      2 2 2
        2 2 2

idx = 0
max_end_day = 0 # 이 값이 겱국 다자라는 날
while idx < len(tree_arr):
    day +=1 하면서
    묘목 하나씩 심는다.
    end_day = day+tree_arr[idx]
    현재 일에 다자라는 날 더해서 갱신여부 확인
    if max_end_day < end_day:
        max_end_day = end_day

1 2 3 4 5 6 7 8
  7 7 7 7 7 7 7
    7 7 7 7 7 7 7
      5 5 5 5 5 5
        2 2 2
          2 2 2

'''
import sys
n = int(sys.stdin.readline())
tree_arr = sorted(list(map(int,sys.stdin.readline().split())),reverse=True)
day = 0
max_end_day = 0
for i in range(n):
    day +=1 # 묘목 심을 때마다 하루는 지나감.
    max_end_day = max(max_end_day,day+tree_arr[i])
print(max_end_day+1)