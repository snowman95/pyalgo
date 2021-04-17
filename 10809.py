import sys
from string import ascii_lowercase
n = sys.stdin.readline().rstrip('\n')
for item in list(ascii_lowercase):
    sys.stdout.write(str(n.find(item)) + " ")