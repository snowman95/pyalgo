# '''
# 코테 개발언어 항목에 cpp, java, python 중 하나를 선택해야 합니다.
# 지원 직군 항목에 backend와 frontend 중 하나를 선택해야 합니다.
# 지원 경력구분 항목에 junior와 senior 중 하나를 선택해야 합니다.
# 선호하는 소울푸드로 chicken과 pizza 중 하나를 선택해야 합니다.
# ----
# [조건]은 "개발언어 and 직군 and 경력 and 소울푸드" 형식의 문자열입니다.
# 언어는 cpp, java, python, - 중 하나입니다.
# 직군은 backend, frontend, - 중 하나입니다.
# 경력은 junior, senior, - 중 하나입니다.
# 소울푸드는 chicken, pizza, - 중 하나입니다.
# '-' 표시는 해당 조건을 고려하지 않겠다는 의미입니다. -> 사실상 *
# X는 코딩테스트 점수를 의미하며 조건을 만족하는 사람 중 
# X점 이상 받은 사람은 모두 몇 명인 지를 의미합니다.


# info
# ["java backend junior pizza 150",
# "python frontend senior chicken 210",
# "python frontend senior chicken 150",
# "cpp backend senior pizza 260",
# "java backend junior chicken 80",
# "python backend senior chicken 50"]

# query
# ["java and backend and junior and pizza 100",
# "python and frontend and senior and chicken 200",
# "cpp and - and senior and pizza 250",
# "- and backend and senior and - 150",
# "- and - and - and chicken 100",
# "- and - and - and - 150"]

# result
# [1,1,1,1,2,4]

# 아이디어
# 집합으로 풀던가
# 저 배열을 집합으로 변환. intersection 해보자.

# info 5만개
# query 10만개
# 개수가 꽤나 많음..

# '''
# info  = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
# #query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# query = ["- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

# def solution(info, query):
#     answer = []
#     info_score = []
#     for index, value in enumerate(info):
#         arr = value.split()
#         info_score.append(int(arr[-1]))
#         info[index] = set(arr[:-1])

#     for index, value in enumerate(query):
#         new_query = set()
#         score = 0
#         pass_cnt = 0
#         for a_index, a_value in enumerate(list(filter(lambda x : x!='and' ,value.split()))):
#             if a_index <= 3:
#                 if a_value == '-' :
#                     if a_index == 0:   new_query.update({'java','cpp','python'})
#                     elif a_index == 1: new_query.update({'backend','frontend'})
#                     elif a_index == 2: new_query.update({'junior','senior'})
#                     elif a_index == 3: new_query.update({'chicken','pizza'})
#                 else: new_query.add(a_value)
#             else:
#                 score = int(a_value)
#         for index, value in enumerate(info):
#             if new_query.issuperset(value) and info_score[index] >= score:
#                 pass_cnt +=1
#         answer.append(pass_cnt)
#     return answer

# solution(info, query)

'''
코테 개발언어 항목에 cpp, java, python 중 하나를 선택해야 합니다.
지원 직군 항목에 backend와 frontend 중 하나를 선택해야 합니다.
지원 경력구분 항목에 junior와 senior 중 하나를 선택해야 합니다.
선호하는 소울푸드로 chicken과 pizza 중 하나를 선택해야 합니다.
----
[조건]은 "개발언어 and 직군 and 경력 and 소울푸드" 형식의 문자열입니다.
언어는 cpp, java, python, - 중 하나입니다.
직군은 backend, frontend, - 중 하나입니다.
경력은 junior, senior, - 중 하나입니다.
소울푸드는 chicken, pizza, - 중 하나입니다.
'-' 표시는 해당 조건을 고려하지 않겠다는 의미입니다. -> 사실상 *
X는 코딩테스트 점수를 의미하며 조건을 만족하는 사람 중 
X점 이상 받은 사람은 모두 몇 명인 지를 의미합니다.


info
["java backend junior pizza 150",
"python frontend senior chicken 210",
"python frontend senior chicken 150",
"cpp backend senior pizza 260",
"java backend junior chicken 80",
"python backend senior chicken 50"]

query
["java and backend and junior and pizza 100",
"python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250",
"- and backend and senior and - 150",
"- and - and - and chicken 100",
"- and - and - and - 150"]

result
[1,1,1,1,2,4]

아이디어
집합으로 풀던가
저 배열을 집합으로 변환. intersection 해보자.

info 5만개
query 10만개
개수가 꽤나 많음..

'''
# import bisect
# info  = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
# query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

# def solution(info, query):
#     answer = []
#     info_box = []
#     score_box = []
#     for index, value in enumerate(info):
#         arr = list(value.split())
#         info_box.append((set(arr[:-1]), int(arr[-1])))

#     info_box.sort(key=lambda x : (x[1],x[0]))
#     info, score_box = zip(*info_box)

#     for index, value in enumerate(query):
#         pass_cnt = 0
#         new_query = list(filter(lambda x : x!='-' and x!='and', value.split()))
#         score = int(new_query[-1])
#         new_query = set(new_query[:-1])
#         binary_search_idx = bisect.bisect_left(score_box, score)
#         for index, information in enumerate(info[binary_search_idx:]):
#             if information.issuperset(new_query):
#                 pass_cnt +=1
#         answer.append(pass_cnt)
#         print(answer)
#     return answer

# solution(info, query)


# import bisect
# info  = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
# query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

# def solution(info, query):
#     answer = []
#     info_box = []
#     score_box = []
#     for index, value in enumerate(info):
#         arr = list(value.split())
#         info_box.append((arr[:-1], int(arr[-1])))

#     info_box.sort(key=lambda x : (x[1],x[0]))
#     info, score_box = zip(*info_box)

#     for index, value in enumerate(query):
#         pass_cnt = 0
#         new_query = value.split(' and ')
#         new_query[-1], score  = new_query[-1].split()
#         score = int(score)

#         # 점수 X 이상인 것
#         binary_search_idx = bisect.bisect_left(score_box, score)
#         # 쿼리 하나에 정보 대입
#         for index, information in enumerate(info[binary_search_idx:]):
#             cnt = 0
#             for i, value in enumerate(information):
#                 if new_query[i] == '-': 
#                     cnt+=1
#                 elif new_query[i] == value:
#                     cnt+=1
#                 else:
#                     break
#             if cnt == 4: 
#                 pass_cnt+=1

#         answer.append(pass_cnt)
#     return answer

# solution(info, query)

import bisect, itertools
info  = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    answer = []
    for index, value in enumerate(info):
        info[index] = list(value.split())
        info[index][-1] = int(info[index][-1])

    info.sort(key=lambda x : x[4])
    arr = [0,1,2,3]

    # new_info["문자열값"] = [오름차순 점수]
    # 사전에 모든 조합을 만들어버림
    new_info = dict()
    for person_info in info:
        combi_arr = set()
        combi_arr.add(''.join(person_info[:-1]))
        score = person_info[-1]
        for i in range(1,5):
            for it in list(itertools.combinations(arr,i)):
                tmp_info = person_info[:-1]
                for idx in it:
                    tmp_info[idx] = '-'
                key = ''.join(tmp_info)
                combi_arr.add(key)
        for key in combi_arr:
            if key not in new_info:
                new_info[key] = [score]
            else : 
                new_info[key].append(score)

    # 쿼리 시작
    for index, value in enumerate(query):
        new_query = value.split(' and ')
        new_query[-1], score  = new_query[-1].split()
        new_query = ''.join(new_query)
        score = int(score)
        size = 0
        # 점수 X 이상인 것
        if new_query in new_info:
            size = len(new_info[new_query]) - bisect.bisect_left(new_info[new_query], score)
        answer.append(size)
    return answer

solution(info, query)