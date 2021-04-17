import sys
from string import ascii_lowercase
n = int(sys.stdin.readline())
sum=0
for i in range(n):
    alpha_list = dict(zip(list(ascii_lowercase), [0]*len(ascii_lowercase)))
    word = sys.stdin.readline().rstrip('\n')
    before = word[0]
    alpha_list[before] = 1
    validation = True
    if word == ''.join(dict.fromkeys(word)):
        sum+=1
    else:
        for i in range(1,len(word)):
            if before != word[i] and alpha_list[word[i]] !=0:
                validation = False
                break
            else:
                before = word[i]
                alpha_list[word[i]] = 1
        if validation == True:
            sum+=1
print(sum)