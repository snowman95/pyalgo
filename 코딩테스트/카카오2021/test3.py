'''
주차장의 요금표와 차량이 들어오고(입차) 나간(출차) 기록이 주어졌을 때, 
차량별로 주차 요금을 계산하려고 합니다. 아래는 하나의 예시를 나타냅니다.

기본 시간(분)	기본 요금(원)	단위 시간(분)	단위 요금(원)
[180, 5000, 10, 600]	

["05:34 5961 IN", "06:00 0000 IN", 
"06:34 0000 OUT", "07:59 5961 OUT", 
"07:59 0148 IN", "18:59 0000 IN", 
"19:09 0148 OUT", "22:59 5961 IN", 
"23:00 5961 OUT"]	

[14600, 34400, 5000]

차량 번호	누적 주차 시간(분)	주차 요금(원)
0000	34 + 300 = 334	5000 + ⌈(334 - 180) / 10⌉ x 600 = 14600
0148	670	5000 +⌈(670 - 180) / 10⌉x 600 = 34400
5961	145 + 1 = 146	5000


1. OUT내역 없다면, 23:59 OUT으로 입력
2. 00:00부터 23:59까지의 입/출차 내역을 바탕으로 
차량별 누적 주차 시간을 계산하여 요금을 일괄로 정산합니다.
3. 
if 주차시간 <= 기본시간 : 기본요금
else :
    기본요금 + math.ceil(초과한시간/단위시간) * 단위요금

차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return 하도록 solution 함수를 완성해주세요.
'''
import math

def get_time(time):
    return int(time[0:2]) * 60 + int(time[3:])

def solution(fees, records):
    answer = []
    base_time, base_cost, standard_time, standard_cost = fees
    car_num_dict = dict()
    car_park_dict = dict()
    car_cost_dict = dict()

    for row in records:
        time, number, inout = row.split()
        if number not in car_num_dict:
            car_num_dict[number] = (0,'00:00')

        if inout == "IN":
            car_num_dict[number] = (time, car_num_dict[number][1])
        else:
            car_num_dict[number] = (car_num_dict[number][0], time)
            if number not in car_park_dict:
                car_park_dict[number] = 0
            car_park_dict[number] += get_time(car_num_dict[number][1]) - get_time(car_num_dict[number][0])

    for number in car_num_dict.keys():
        if car_num_dict[number][1] == '00:00' or car_num_dict[number][0] > car_num_dict[number][1]:
            car_num_dict[number] = (car_num_dict[number][0], '23:59')
            if number not in car_park_dict:
                car_park_dict[number] = 0
            car_park_dict[number] += get_time(car_num_dict[number][1]) - get_time(car_num_dict[number][0])

    for number in car_num_dict.keys():
        park_time = car_park_dict[number]
        if number not in car_cost_dict:
            car_cost_dict[number] = 0
        if park_time <= base_time:
            car_cost_dict[number] = base_cost
        else:
            car_cost_dict[number] = base_cost + math.ceil((park_time-base_time)/standard_time) * standard_cost

    result = []
    for number in car_cost_dict.keys():
        result.append((number, car_cost_dict[number]))
    result.sort(key= lambda x : (x[0]))
    for number,cost in result:
        answer.append(cost)
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
solution(fees, records)