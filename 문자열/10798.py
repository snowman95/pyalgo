'''
A~Z
a~z
0~9
걍 세로로로 줄줄이 읽으면 됨요 (한 줄에 최대15자)
AABCDD
afzz
09121
a8EWg6
P5h3kx

Aa0aPAf985Bz1EhCz2W3D1gkD6x

아이디어
배열 5개에 입력받고, 세로로 읽어내린다.
'''
import sys
arr = [sys.stdin.readline().strip() for _ in range(5)]
for i in range(5):
    arr[i] += '!'*15
for col in range(15):
    for row in range(5):
        if arr[row][col] != '!':
            sys.stdout.write(arr[row][col])