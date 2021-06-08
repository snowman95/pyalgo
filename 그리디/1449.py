import sys
n,l = map(int,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
tape = [False] * 2001
tape_cnt = 0
for i in range(n):
    cur = arr[i]
    if not tape[cur]:
        tape[cur:cur+l] = [True] * l
        tape_cnt +=1
print(tape_cnt)