import sys
n = int(sys.stdin.readline())
n = sys.stdin.readline().rstrip('\n')
sum = 0
for item in n:
    sum += int(item)
print(sum)