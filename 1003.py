import sys
import operator
fibo_arr = [[1,0],[0,1],[1,1],[1,2]] + [0] * 37

for n in range(4, 41):
    fibo_arr[n] = list(map(operator.add, fibo_arr[n-1], fibo_arr[n-2]))

T = int(sys.stdin.readline())
for a in range(T):
    i = int(sys.stdin.readline())
    print(fibo_arr[i][0], fibo_arr[i][1])