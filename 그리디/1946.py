# import sys

# T = int(sys.stdin.readline())
# for t in range(T):
#     n = int(sys.stdin.readline())
#     first, second = [], []
#     for i in range(n):
#         a,b = map(int, sys.stdin.readline().split())
#         first.append((a,b))
#         second.append((b,a))
#     first.sort(reverse=True)
#     second.sort()

#     cnt = 0
#     for rank in first:
#         valid = True
#         for sec_rank in range(rank[1]-1):
#             if rank[0] < second[sec_rank][0]:
#                 valid = False
#                 break
#         if valid:
#             cnt+=1
#     print(cnt)


# import sys

# T = int(sys.stdin.readline())
# for t in range(T):
#     n = int(sys.stdin.readline())
#     rank = []
#     for i in range(n):
#         a,b = map(int, sys.stdin.readline().split())
#         rank.append((a,b))
#     cnt = 0
#     for i in range(n):
#         valid = True
#         for j in range(n):
#             if i == j:
#                 continue
#             if rank[i][0] > rank[j][0] and rank[i][1] > rank[j][1]:
#                 valid = False
#                 break
#         if valid:
#             cnt+=1
#     print(cnt)



import sys

T = int(sys.stdin.readline())
for t in range(T):
    n = int(sys.stdin.readline())
    rank = list(tuple(map(int, sys.stdin.readline().split())) for _ in range(n))
    rank.sort()
    cnt = 1
    minimum = rank[0][1]
    for i in range(1,n):
        if rank[i][1] < minimum:
            minimum = rank[i][1]
            cnt+=1
    print(cnt)