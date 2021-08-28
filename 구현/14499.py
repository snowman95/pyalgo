'''
주사위 굴리기

크기 NxM 지도 
좌표는 (r,c)

지도 위에 윗면이 1, 동쪽이 3 인 상태로 놓여있고
처음에 모든 면에 0이 적혀있다.
  2
4 1 3
  5
  6

if 주사위 굴렀을때 이동한 칸의 수 == 0 이면
    주사위 바닥면의 수 → 칸의 수
else :
    칸의 수 → 주사위 바닥면의 수

이동명령 :  동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.
이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력
지도 바깥으로 이동 하면 안됨. 이동하라고 하면 아무것도 하지말도록 출력도 x

[아이디어]
6면을 가진 주사위 자료구조 생성
4방향으로 굴러갈때의 값 업데이트

'''
import sys

# 북,동,남,서,위,아래
d = {
    "북":0,
    "동":1,
    "남":2,
    "서":3,
    "위":4,
    "아래":5,
}
roll = (
    (),
    ("동","위","서","아래"),
    ("서","위","동","아래"),
    ("북","위","남","아래"),
    ("남","위","북","아래"),
)

n,m,x,y,k = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
command = map(int,sys.stdin.readline().split())
dice = [0]*6
dx = (0,0,0,-1,1)
dy = (0,1,-1,0,0)
for c in command:
    nx = dx[c]+x
    ny = dy[c]+y
    if 0<=nx<n and 0<=ny<m :
        x = nx
        y = ny
        tmp = dice[d[roll[c][0]]]
        for i in range(1,4):
            old = d[roll[c][i-1]]
            new = d[roll[c][i]]
            dice[old] = dice[new]

        if board[nx][ny] == 0:
            dice[d["아래"]] = tmp
            board[nx][ny] = tmp
        else:
            dice[d["아래"]] = board[nx][ny]
            board[nx][ny] = 0
            
        print(dice[d["위"]])