import sys
'''
0~9, +,-
-(...)-(...) 이런 형태가 최소가 됨
'''
word = sys.stdin.readline().rstrip()
int_word = ''
tmp = ''
minus = False
for w in word:
    if w == '-':
        minus = True
        if tmp !='':
            int_word += str(int(tmp)) + w
        if int_word =='':
            int_word = w
        tmp = ''
    elif w == '+':
        if minus:
            w = '-'
        if tmp !='':
            int_word += str(int(tmp)) + w
        tmp = ''
    else :
        tmp += w
if tmp != '':
    int_word += str(int(tmp))
print(eval(int_word))