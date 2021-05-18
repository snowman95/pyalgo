import sys

T = int(sys.stdin.readline())

koong = [0]*68
for n in range(68):
    if n<2:
        koong[n] = 1
    elif n==2:
        koong[n] = 2
    elif n==3:
        koong[n] = 4
    else:
        koong[n] = koong[n-1] + koong[n-2] + koong[n-3] + koong[n-4]
for t in range(T):
    print(koong[int(sys.stdin.readline())])