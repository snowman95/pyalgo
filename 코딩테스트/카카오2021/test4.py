'''
어피치가 화살 n발을 다 쏜 후에 라이언이 화살 n발을 쏩니다.

가장 작은 원의 과녁 점수는 10점이고 
가장 큰 원의 바깥쪽은 과녁 점수가 0점입니다.
10,9,8,...,0

k(1~10)점을 어피치가 a발

라이언이 b발

더 많은 화살을 k점에 맞힌 선수가 k 점을 가져갑니다. 

단, a = b일 경우는 어피치가 k점을 가져갑니다. 

a = 어피치 k점 맞춘 횟수
b = 라이언 k점 맞춘 횟수

if a!=0 and b!=0:
    if a>=b : 어피치 += k점
    else : 라이언 += k점

예를 들어, 어피치가 10점을 2발 맞혔고 라이언도 10점을 2발 맞혔을 경우 어피치가 10점을 가져갑니다.
다른 예로, 어피치가 10점을 0발 맞혔고 라이언이 10점을 2발 맞혔을 경우 라이언이 10점을 가져갑니다.
모든 과녁 점수에 대하여 각 선수의 최종 점수를 계산합니다.
최종 점수가 더 높은 선수를 우승자로 결정합니다. 단, 최종 점수가 같을 경우 어피치를 우승자로 결정합니다.


현재 상황은 어피치가 화살 n발을 다 쏜 후이고 라이언이 화살을 쏠 차례입니다.
라이언은 어피치를 가장 큰 점수 차이로 이기기 위해서 n발의 화살을 어떤 과녁 점수에 맞혀야 하는지를 구하려고 합니다.

화살의 개수를 담은 자연수 n, 
어피치가 맞힌 과녁 점수의 개수를 10점부터 0점까지 순서대로 담은 정수 배열 info가 매개변수로 주어집니다.

이때, 라이언이 "가장 큰" 점수 차이로 우승하기 위해 
n발의 화살을 어떤 과녁 점수에 맞혀야 하는지를 10점부터 0점까지 순서대로 정수 배열에 담아 return 하도록
solution 함수를 완성해 주세요. 
만약, 라이언이 우승할 수 없는 경우(무조건 지거나 비기는 경우)는 [-1]을 return 해주세요.

n	info	result
5	[2,1,1,1,0,0,0,0,0,0,0]	[0,2,2,0,1,0,0,0,0,0,0]
1	[1,0,0,0,0,0,0,0,0,0,0]	[-1]
9	[0,0,1,2,0,1,1,1,1,1,1]	[1,1,2,0,1,2,2,0,0,0,0]
10	[0,0,0,0,0,0,0,0,3,4,3]	[1,1,1,1,1,1,1,1,0,0,2]


어피치가
10,9,8,7,6,5,4,3,2,1,0점 을 몇번 맞혔는지
[2,1,1,1,0,0,0,0,0,0,0]

라이언이 아래와 같이 하면 됨
[0,2,2,0,1,0,0,0,0,0,0]



[아이디어 회의]
그리드 혹은 DP 혹은 조합냄새

dp[n] = n번 과녁을 맞혔을때


그리드 - 아니야 그냥 가능한 횟수를 count해보자.
라이언은 점수별로 적어도 아래 개수만큼은 맞혀야 점수를 가져갈 수 있습니다.
10,9,8,7,6,5,4,3,2,1,0점 을 몇번 맞혔는지
[3,2,2,2,1,1,1,1,1,1,1]

10,9,8,7,6
3+2 = 5(n=5) 면 19점

정답은
[0,2,2,0,1,0,0,0,0,0,0]

모든 조합을 구해보자.
개수는 1,2,3중에 n개를 조합할거임.
예를들어 아래와 같이 모든 가능한 조합을 구해보는 것임.
2+3
1+1+3
1+1+1+2
1+1+1+1+1

'''

# BFS 기본형태
from collections import deque

def solution(n, info):
    answer = []
    numbers = [0,1,2,3,4,5,6,7,8,9]
    a_score = 0 # 최대점수
    for i in range(10):
        if info[i]!=0:
           a_score += 10-i

    b_need_info = list(map(lambda x : x+1, info))
    b_need_info_set = set(map(lambda x : x+1, info))
    try_arr = []
    q = deque()
    for i in b_need_info_set:
        q.append((i,[i]))
    while q:
        cnt, track = q.popleft()
        if cnt == n:
            try_arr.append(track)
            continue
        for i in b_need_info_set:
            if cnt+i <=n :
                q.append((cnt+i, track+[i]))
    max_score = -1
    total_min_hit = 11
    total_max_cnt = 0
    answer = []
    for row in try_arr:
        idx = 0
        a_tmp_score = a_score
        b_score = 0
        arr = [0] * 11
        visited = [False] * 11
        cnt = 0
        for hit in sorted(row, reverse=True):
            for idx, need_hit in enumerate(b_need_info):
                if idx == 10:
                    continue
                if need_hit == hit and not visited[idx]:
                    visited[idx] = True
                    b_score += 10-idx
                    if info[idx] != 0:
                        a_tmp_score -= 10-idx
                    arr[idx] += hit
                    cnt += hit
                    break
        arr[10] = n-sum(arr)
        if max_score < b_score-a_tmp_score:
            min_hit_value = 11
            max_cnt = 0
            for idx, value in enumerate(arr[::-1]):
                if value != 0:
                    min_hit_value = idx
                    max_cnt = value
                    break
            total_min_hit = min_hit_value
            total_max_cnt = max_cnt
            max_score = b_score-a_tmp_score
            answer = arr
            
        elif max_score == b_score-a_tmp_score:
            min_hit_value = 11
            max_cnt = 0
            for idx, value in enumerate(arr[::-1]):
                if value != 0:
                    min_hit_value = idx
                    max_cnt = value
                    break
            if total_min_hit > min_hit_value:
                total_min_hit = min_hit_value
                max_score = b_score-a_tmp_score
                answer = arr
            elif total_min_hit == min_hit_value:
                if total_max_cnt < max_cnt:
                    total_max_cnt = max_cnt
                    max_score = b_score-a_tmp_score
                    answer = arr

    if not answer or max_score == -1 or max_score == 0:
        answer = [-1]
    return answer
'''

b_score 39 a_tmp_score 10 b_score-a_tmp_score 29
[1, 0, 2, 0, 0, 2, 2, 2, 0, 0, 0]

[1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0]
b_score 42 a_tmp_score 13 b_score-a_tmp_score 29


'''
n = 10
info = [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]
solution(n, info)