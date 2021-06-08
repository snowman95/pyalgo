import sys
word = sys.stdin.readline().rstrip('\n').upper()
word_set  = set(word)
word_dict = dict(zip(word_set, [0]*len(word_set)))
for w in word:
    word_dict[w]+=1

v = word_dict.values()
max_v = max(v)
cnt = list(word_dict.values()).count(max_v)
if cnt > 1:
    print('?')
else:
    for w in word_dict.items():
        if w[1] == max_v:
            print(w[0])
            break
