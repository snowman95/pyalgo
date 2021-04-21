import sys
n = int(sys.stdin.readline())
words = []
for i in range(n):
    tmp = sys.stdin.readline().rstrip().split()
    words.append((int(tmp[0]),i,tmp[1]))

words.sort()
for w in words:
    sys.stdout.write(str(w[0]) + ' ' + w[2] + '\n')