import sys
from string import ascii_uppercase
d = dict(zip(list(ascii_uppercase), [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]))
n = sys.stdin.readline().rstrip('\n')
sum=0
for i in n:
    sum +=d[i]
print(sum)