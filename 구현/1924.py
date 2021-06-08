import sys
x,y = map(int, sys.stdin.readline().split())
day_cnt = (31,28,31,30,31,30,31,31,30,31,30,31)
day = ("SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT")
total_day = y
for i in range(1,x):   
    total_day += day_cnt[i-1]
print(day[total_day%7])