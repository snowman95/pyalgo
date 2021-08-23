'''
홀수

7개의 자연수,
이들 중 홀수인 자연수는 합하고, 홀수중 최소값 구해라
'''
import sys
arr = list(filter(lambda x: x%2==1, [int(sys.stdin.readline()) for i in range(7)]))
if arr:
    (1,2)
    print(sum(arr), min(arr), sep="\n")
else:
    print(-1)