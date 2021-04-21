import sys
import collections
n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()) + 4000)

mode = collections.Counter(array).most_common()
mode_len = len(mode)
ans = mode[0][0] - 4000
first_mode = mode[0][1]
if mode_len > 1:
    m = [ans]
    for i in range(1, mode_len):
        if first_mode == mode[i][1]:
            m.append(mode[i][0]-4000)
    m.sort()
    if len(m) > 1:
        ans = m[1]

print(round(sum(array)/len(array))-4000)
array.sort()
print(int(array[int(len(array)/2)])-4000)
print(ans)
print(max(array)-min(array))