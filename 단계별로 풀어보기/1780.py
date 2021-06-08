import sys
n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
paper_cnt = [0,0,0]
def color_check(x,y,length):
    global color
    color = paper[x][y]
    for i in range(length):
        for j in range(length):
            if paper[x+i][y+j] != color:
                return -100
    return color+1
def split_paper(x,y,length):
    c = color_check(x,y,length)
    if c != -100:
        paper_cnt[c]+=1
        return 
    length //=3
    for i in range(3):
        for j in range(3):
            split_paper(x+length*i,y+length*j, length)
        
split_paper(0,0,n)
for c in paper_cnt:
    print(c)