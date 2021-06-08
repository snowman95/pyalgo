import sys, string
A = ord('A')
n = int(sys.stdin.readline())
board = [0] * len(string.ascii_uppercase)
for i in range(n):
    arr = sys.stdin.readline().strip()
    size = len(arr)
    for j in range(size):
        board[ord(arr[j])-A] += int(pow(10,size-j-1))

ans, num = 0,9
board.sort(reverse=True)
for item in board:
    if item != 0:
        ans += item * num
        num-=1
print(ans)