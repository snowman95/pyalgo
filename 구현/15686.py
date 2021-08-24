'''
치킨 배달

NxN 도시 (r,c) ※ 1부터 시작됨
0 빈칸
1 집
2 치킨집

치킨거리 = 집과 가장 가까운 치킨집까지 거리
도시치킨거리 = sum(모든 치킨거리)
(r1, c1)과 (r2, c2) 거리 = |r1-r2| + |c1-c2|

도시치킨거리가 최소화되도록 도시의 치킨집 최대 M개 빼고 나머지 모두폐업시켜라.

[초기화]
각 집의 좌표를 저장
house_pos_arr = [] 

[메인 로직]
1. chick_house_cnt 중에서 1개~M개 만큼 치킨집을 선택 : dfs활용
2. for h in house_pos_arr : # 각 집에서 치킨집까지의 거리

min(치킨집 1개만 있을경우 도시치킨거리 ~ 치킨집 M개만 있을경우의 도시치킨거리)


'''
# import itertools
# import sys
# from itertools import permutations

# house_pos_arr = []
# chick_pos_arr = []
# min_dist = 9999999999
# def get_city_chick_dist(arr):
#     global chick_pos_arr, house_pos_arr, min_dist
#     total_dist = 0
#     for hx,hy in house_pos_arr:
#         dist = 9999999999
#         for i in arr:
#             cx,cy = chick_pos_arr[i]
#             dist = min(dist,abs(hx-cx) + abs(hy-cy))
#         total_dist+=dist
#     min_dist = min(min_dist, total_dist)
#     return

# def select_chick_house(arr, goal_cnt, total_size, cur_cnt=0, seq=0):
#     if goal_cnt == cur_cnt:
#         get_city_chick_dist(arr)
#         return
#     if total_size <= seq:
#         return
#     arr.append(seq)
#     select_chick_house(arr,goal_cnt,total_size,cur_cnt+1,seq+1)
#     arr.pop()
#     select_chick_house(arr,goal_cnt,total_size,cur_cnt,seq+1)
#     return

# n,m = map(int, sys.stdin.readline().split())
# board = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
# for x in range(n):
#     for y in range(n):
#         if board[x][y] == 1:
#             house_pos_arr.append((x,y))
#         elif board[x][y] == 2:
#             chick_pos_arr.append((x,y))

# for i in range(1,m+1):
#     #data = itertools.combinations(chick_pos_arr,i)
#     #print(list(data))
#     select_chick_house([],goal_cnt=i,total_size=len(chick_pos_arr))
# print(min_dist)


# 아래는 combinations 사용한 것
import itertools
import sys

min_dist = 9999999999
n,m = map(int, sys.stdin.readline().split())
board = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

house_pos_arr = []
chick_pos_arr = []
for x in range(n):
    for y in range(n):
        if board[x][y] == 1:   house_pos_arr.append((x,y))
        elif board[x][y] == 2: chick_pos_arr.append((x,y))

for i in range(1,m+1):
    selected_chick = list(itertools.combinations(chick_pos_arr,i))
    for chick_arr in selected_chick:
        min_chick_dist = 0
        for hx,hy in house_pos_arr:
            chick_dist = sys.maxsize
            for cx,cy in chick_arr:
                chick_dist = min(chick_dist, abs(hx-cx) + abs(hy-cy))
            min_chick_dist +=chick_dist
        min_dist = min(min_dist,min_chick_dist)
                
print(min_dist)