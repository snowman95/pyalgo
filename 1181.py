import sys
n = int(sys.stdin.readline())
words = {sys.stdin.readline().rstrip() for _ in range(n)}
w = list(zip([len(w) for w in words], words))
w.sort()
for i in w:
    print(i[1])