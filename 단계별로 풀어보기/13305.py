import sys
'''
일직선 상의 n개 도시 순서대로 이동 (n: 2~10만)
도시 간의 도로길이 km로 주어짐 (1km이동 당 1리터 기름 사용)
도시 마다 기름 가격 다름

입력
도시 개수 n
도로길이 순서대로
주유소 리터당 가격

출력
모든 도시 이동하는 최소 비용

싼 도시에서 기름을 많이 구입하는게 이득.

1번도시에서는 무조건 기름 구매해야 함.
뒤의 도시에서 더 저렴하게 기름 구매할 수 있으면 1→2 이동하는 만큼만 구매하면 됨.

마지막 도시는 제외하고 나보다 기름값이 싼 도시까지의 기름을 사면됨.
'''
n = int(sys.stdin.readline())
road_len = list(map(int, sys.stdin.readline().split()))
oil_price = list(map(int, sys.stdin.readline().split()))

cur_oil_price = oil_price[0]
total_price = 0
tmp_road_len = road_len[0]
for i in range(1, n-1):
    if cur_oil_price <= oil_price[i]:
        tmp_road_len += road_len[i]
    else :
        total_price += tmp_road_len * cur_oil_price
        cur_oil_price = oil_price[i]
        total_price += road_len[i] * cur_oil_price
        tmp_road_len = 0
        
if tmp_road_len != 0:
        total_price += tmp_road_len * cur_oil_price
print(total_price)