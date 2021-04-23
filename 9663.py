import sys
n = int(sys.stdin.readline())
ans = 0
def choice(row, pos, col_visit):
    if row == n:
        global ans
        ans+=1
        return
    for col in range(n):
        if col_visit[col]:
            continue
        cross_check = True
        for p in pos:
            if abs(row-p[0]) == abs(col-p[1]):
                cross_check = False
                break
        if cross_check == False:
            continue
        col_visit[col] = True
        pos.append((row,col))
        choice(row+1, pos, col_visit)
        pos.pop()
        col_visit[col] = False
        
choice(0,[], [False]*n)
print(ans)