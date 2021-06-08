import sys

def hotel(h,w,n):
    for i in range(1,w+1):
        for j in range(1,h+1):
            room_num = 100*j+i
            n-=1
            if n==0:
                return room_num

T = int(sys.stdin.readline())
for t in range(T):
    h,w,n = map(int,sys.stdin.readline().split())
    print(hotel(h,w,n))