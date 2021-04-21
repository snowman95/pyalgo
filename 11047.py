import sys
'''
동전 N개 중 최소개수로 가치합을 k로
'''
n,k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
coin_cnt = 0
cur_idx = n-1
while True:
    if k == 0 or cur_idx < 0:
        break
    cnt = k//coins[cur_idx]
    if cnt >=0:
        k -= cnt * coins[cur_idx]
        coin_cnt += cnt
    cur_idx-=1
print(coin_cnt)