import sys
n, m = map(int,sys.stdin.readline().split())
hear = {sys.stdin.readline().rstrip() for _ in range(n)}
see = {sys.stdin.readline().rstrip() for _ in range(m)}
hear_see = hear.intersection(see)
print(len(hear_see))
for i in sorted(hear_see):
    print(i)