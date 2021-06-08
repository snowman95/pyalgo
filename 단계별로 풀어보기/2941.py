import sys
word = sys.stdin.readline().rstrip()
a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in a:
    word = word.replace(i, '_')
print(len(word))