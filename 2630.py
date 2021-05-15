import sys
n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
paper_cnt = [0,0]
def color_check(x,y,length):
    global color
    color = paper[x][y]
    for i in range(length):
        for j in range(length):
            if paper[x+i][y+j] != color:
                return -1
    return color
def split_paper(x,y,length):
    c = color_check(x,y,length)
    if c != -1:
        paper_cnt[c]+=1
        return 
    length //=2
    split_paper(x,y,length)
    split_paper(x+length,y,length)
    split_paper(x,y+length,length)
    split_paper(x+length,y+length,length)
        
split_paper(0,0,n)
for c in paper_cnt:
    print(c)