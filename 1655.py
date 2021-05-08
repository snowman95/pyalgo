import sys, heapq
n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
lheap = [] # max_heap
rheap = [] # min_heap
lsize = 0
rsize = 0
mid = (nums[0], nums[0])
sys.stdout.write(str(mid[1])+'\n')

for i in range(1,n):
    if mid[1] <= nums[i]:
        rsize +=1
        heapq.heappush(rheap,(nums[i],nums[i]))
    else:
        lsize +=1
        heapq.heappush(lheap,(-nums[i],nums[i]))
    
    if i%2 == 0:
        comp = lsize
    else :
        comp = lsize+1
    if comp < rsize:
        heapq.heappush(lheap, (-mid[1],mid[1]))
        mid = heapq.heappop(rheap)
        lsize +=1
        rsize -=1
    elif lsize > rsize:
        heapq.heappush(rheap, (mid[1],mid[1]))
        mid = heapq.heappop(lheap)
        lsize -=1
        rsize +=1

    sys.stdout.write(str(mid[1])+'\n')