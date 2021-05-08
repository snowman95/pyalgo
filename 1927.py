import sys, heapq
n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
heap = []
for i in nums:
    if i == 0:
        if heap: print(heapq.heappop(heap))
        else: print(0)
    else:
        heapq.heappush(heap,i)