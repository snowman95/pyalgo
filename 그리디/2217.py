import sys

n = int(sys.stdin.readline())
rope = [int(sys.stdin.readline()) for _ in range(n)]
rope.sort(reverse=True)
weight = 0
for i in range(n):
    weight = max(weight,rope[i]*(i+1))
print(weight)