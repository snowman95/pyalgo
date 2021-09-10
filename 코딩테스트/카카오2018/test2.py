'''
실패율
전체 스테이지의 개수 N, 
게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

실패율은 다음과 같이 정의한다.
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

N	stages	result
5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
4	[4,4,4,4,4]	[4,1,2,3]

n = 스테이지 갯수
각 사용자의 현재 스테이지 번호
만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.

실패율 높은 스테이지 내림차순.
같은 실패율일땐 작은 번호가 앞으로

스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

오름차순 정렬하고, 이분탐색으로 찾음
'''
import bisect
def solution(N, stages):
    answer = []
    tmp = []

    stages.sort()
    fail_man = 0
    total_man = len(stages)
    for i in range(1, N+1):
        fail_cnt = bisect.bisect_right(stages, i)# 몇 명

        if total_man == fail_man :
            fail_percent = 0
        else:
            fail_percent = fail_cnt / (total_man-fail_man)
        stages = stages[fail_cnt:]
        fail_man += fail_cnt
        tmp.append((fail_percent, -i))

    # x[0]이 큰 순서. x[1]이 작은 순서로 정렬해야함
    tmp.sort(reverse=True)
    for f, idx in tmp:
        answer.append(-idx)
    return answer

n = 5
s = [2, 1, 2, 6, 2, 4, 3, 3]
solution(n, s)