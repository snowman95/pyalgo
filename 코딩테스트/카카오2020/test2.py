# '''
# 코스요리는 최소 2가지이상의 단품메뉴로 구성됨
# 최소 2명 이상의 손님으로 부터 주문된 단품메뉴 조합만 코스에 포함

# 각 손님은 2개 이상 단품메뉴 주문
# 메뉴 : A~Z

# 손님 번호	주문한 단품메뉴 조합
# 1번 손님	A, B, C, F, G
# 2번 손님	A, C
# 3번 손님	C, D, E
# 4번 손님	A, C, D, E
# 5번 손님	B, C, F, G
# 6번 손님	A, C, D, E, H

# 코스 종류	메뉴 구성	설명
# 요리 2개 코스	A, C	1번, 2번, 4번, 6번 손님으로부터 총 4번 주문됐습니다.
# 요리 3개 코스	C, D, E	3번, 4번, 6번 손님으로부터 총 3번 주문됐습니다.
# 요리 4개 코스	B, C, F, G	1번, 5번 손님으로부터 총 2번 주문됐습니다.
# 요리 4개 코스	A, C, D, E	4번, 6번 손님으로부터 총 2번 주문됐습니다.

# 방법 1. 손님마다 AB AC AF AG ABC ABF ABG ACF ACG AFG ABCF ABCG 이런식으로
# 조합을 만들어둔다. → 근데 너무 오래 걸리듯 최대 10개라
# 다른 손님이 해당 조합 포함하면 result 추가

# 방법 2. 집합으로 푼다.
# 이거 1~n번 손님까지 반복하면서 합집합 구해둠.


# '''
# import itertools

# def solution(orders, course):
#     set_orders = []
#     answer = [] 
#     tmp = []
#     for o in orders:
#         set_orders.append(set(o))
#     size = len(set_orders)
#     for i in range(size):
#         for j in range(i+1, size):
#             inter_arr = set_orders[i].intersection(set_orders[j])
#             if len(inter_arr) in course:
#                 tmp.append(''.join(inter_arr))
#     tmp.sort()
#     for i in range(len(tmp)):
#         tmp[i] = ''.join(sorted(tmp[i]))

#     # ACB -> AC AB CB 와 같이 쪼개는 과정
#     extend_tmp = tmp
#     for t in tmp:
#         for c in course:
#             if len(t) <= c: break
#             for k in list(itertools.combinations(t,c)):
#                 extend_tmp.append(''.join(k))

#     # 각 요소들의 개수를 count 하여 가장 많이 등장한 것 확인
#     #if len(extend_tmp != len(tmp)):
#     course_arr = dict()
#     for c in course: 
#         course_arr[c] = []
#     for item in set(extend_tmp):
#         course_arr[len(item)].append((extend_tmp.count(item),item))

#     for i, c in list(course_arr.items()):
#         max_cnt = 0
#         arr = []
#         if c:
#             for size, item in c:
#                 if max_cnt < size:
#                     max_cnt = size
#                     arr.clear()
#                     arr = [item]
#                 elif max_cnt == size:
#                     arr.append(item)
#             answer+=arr

#     print(sorted(answer))
# o = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# c = [2,3,4,5]
# solution(o,c)


'''
코스요리는 최소 2가지이상의 단품메뉴로 구성됨
최소 2명 이상의 손님으로 부터 주문된 단품메뉴 조합만 코스에 포함

각 손님은 2개 이상 단품메뉴 주문
메뉴 : A~Z

손님 번호	주문한 단품메뉴 조합
1번 손님	A, B, C, F, G
2번 손님	A, C
3번 손님	C, D, E
4번 손님	A, C, D, E
5번 손님	B, C, F, G
6번 손님	A, C, D, E, H

코스 종류	메뉴 구성	설명
요리 2개 코스	A, C	1번, 2번, 4번, 6번 손님으로부터 총 4번 주문됐습니다.
요리 3개 코스	C, D, E	3번, 4번, 6번 손님으로부터 총 3번 주문됐습니다.
요리 4개 코스	B, C, F, G	1번, 5번 손님으로부터 총 2번 주문됐습니다.
요리 4개 코스	A, C, D, E	4번, 6번 손님으로부터 총 2번 주문됐습니다.

방법 1. 손님마다 AB AC AF AG ABC ABF ABG ACF ACG AFG ABCF ABCG 이런식으로
조합을 만들어둔다. → 근데 너무 오래 걸리듯 최대 10개라
다른 손님이 해당 조합 포함하면 result 추가

방법 2. 집합으로 푼다.
이거 1~n번 손님까지 반복하면서 합집합 구해둠.


'''
# import itertools

# def solution(orders, course):
#     answer = [] 
#     tmp = []
#     set_orders = list(map(set, orders))
#     size = len(set_orders)
#     for i in range(size):
#         for j in range(i+1, size):
#             inter_arr = set_orders[i].intersection(set_orders[j])
#             if len(inter_arr) in course:
#                 inter_arr = sorted(inter_arr)
#                 tmp.append(''.join(inter_arr))
#                 for c in course:
#                     if len(inter_arr) <= c: break
#                     for k in list(itertools.combinations(inter_arr,c)):
#                         tmp.append(''.join(k))
#     tmp.sort()
#     # 각 요소들의 개수를 count 하여 가장 많이 등장한 것 확인
#     course_arr = dict()
#     for c in course: 
#         course_arr[c] = []
#     for item in set(tmp):
#         course_arr[len(item)].append((tmp.count(item),item))

#     for i, c in list(course_arr.items()):
#         max_cnt = 0
#         arr = []
#         if c:
#             for size, item in c:
#                 if max_cnt < size:
#                     max_cnt = size
#                     arr = [item]
#                 elif max_cnt == size:
#                     arr.append(item)
#             answer+=arr

#     print(sorted(answer))
# o = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# c = [2,3,4]
# solution(o,c)


import itertools

def solution(orders, course):
    answer = [] 
    orders = list(map(set, orders))
    order_combinations = []
    menu_dict = dict()
    for cnt in course: 
        menu_dict[cnt] = []

    for menu in orders:
        size = len(menu)
        for cnt in course:
            if cnt < size:
                items = list(map(''.join, list(itertools.combinations(sorted(menu),cnt))))
                order_combinations += items
            elif cnt == size:
                order_combinations.append(''.join(sorted(menu)))

    for item in set(order_combinations):
        cnt = order_combinations.count(item)
        if cnt >=2 :
            menu_dict[len(item)].append((cnt,item))
    # 각 요소들의 개수를 count 하여 가장 많이 등장한 것 확인

    for i, c in list(menu_dict.items()):
        max_cnt = 0
        arr = []
        for cnt, menu in c:
            if max_cnt < cnt:
                max_cnt = cnt
                arr = [menu]
            elif max_cnt == cnt:
                arr.append(menu)
        answer+=arr

    print(sorted(answer))
o = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
c = [2,3,5]
solution(o,c)