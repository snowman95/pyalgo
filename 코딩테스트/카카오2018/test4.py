'''
무지의 먹방 라이브

회전판에 먹어야 할 N 개의 음식 (1~N번)


무지는 1번 음식부터 먹기 시작하며, 
회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓는다.
마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 온다.

무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취한다.
다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식을 말한다.
회전판이 다음 음식을 무지 앞으로 가져오는데 걸리는 시간은 없다고 가정한다.


k 초 후에 방송 중단된다. 그 이후에 몇번 음식 먹어야 되는지 구하기
k 는 방송이 중단된 시간을 나타낸다.
각 음식을 모두 먹는데 필요한 시간이 담겨있는 배열 food_times,

음식 20만개 배열 (원소는 1~1억까지 숫자)

- 초당 1회 음식 섭취
- 
[3,1,2]

오름차순 정렬 후 작은 순서대로 진행
300 100 200 인 경우
100 200 300 정렬하고 100초 지났을 경우
0 100 200 이렇게 되므로 100초 이후에는 100 200 둘이서 진행하게 된다.
만약 k초 보다 

3 1 2 같은 경우
[1 2 3] 순서니
1회*3개*초 = 3초 이후 : 0 1 2 이렇게 됨. 

- sort()음식시간 오름차순 정렬
- for idx in 
- cnt 하면서, 다음 idx값에서 arr[inx]-cnt 이렇게하셈

'''
def solution(food_times, k):
    answer = -1
    if k >= sum(food_times):
        return answer
    total_food_size = len(food_times)
    pass_time = 0
    last_food_time = 0
    sorted_food_times = sorted(food_times)
    sorted_food_times_idx = -1
    for idx, cur_food_time in enumerate(sorted_food_times):
        plus_time = (cur_food_time-last_food_time) * (total_food_size-idx)
        if pass_time + plus_time > k:
            break
        pass_time += plus_time
        last_food_time = cur_food_time
        sorted_food_times_idx = idx

    final_foods = []
    for idx, food in enumerate(food_times):
        last = food-last_food_time
        if last > 0:
            final_foods.append((last,idx))
    if pass_time < k:
        remain_time = k-pass_time
        last_food_cnt = total_food_size-(sorted_food_times_idx+1)
        if final_foods and last_food_cnt != 0:
            answer = final_foods[remain_time % last_food_cnt][1]+1
    else:
        answer = final_foods[0][1]+1
    return answer

food_times = [3,1,2]# [1,2,3,4,5]
k = 5
print(solution(food_times, k))