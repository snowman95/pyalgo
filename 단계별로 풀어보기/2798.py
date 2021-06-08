import sys
'''
N장 카드 중 3개 택해서 M을 넘지않으면서가장 큰 수
'''
def choice(cnt, choice_cnt, card_sum, visit):
    global n
    global m
    global cards
    global max_value
    if choice_cnt == 3 and card_sum <= m:
        max_value = max(max_value, card_sum)
        return
    if cnt == n or card_sum > m or choice_cnt > n:
        return
    if visit[cnt]:
        choice(cnt+1, choice_cnt, card_sum, visit)
    else:
        visit[cnt] = True
        choice(cnt+1, choice_cnt+1, card_sum+cards[cnt],visit)
        visit[cnt] = False
        choice(cnt+1, choice_cnt, card_sum, visit)

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
max_value = 0
choice(1, 0, 0, [False]*n)
print(max_value)