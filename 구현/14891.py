'''
톱니바퀴
8개의 톱니를 가진 톱니바퀴 4개 1,2,3,4 번

k번 회전 시킨다. (시계/반시계)
맞닿은 톱니바퀴는 반대로 회전한다.

두 가지 경우밖에 없음
1234
rlrl

1234
lrlr

톱니 k번 회전하고나서의 상태 출력

[톱니 상태 저장 방법]
덱으로 구현한다. 12시 1시 2시..순으로 저장해 그냥

[구현 순서]
1. n번 톱니를 돌렸을때 1234 톱니 상태 업데이트 함수
g1[2] != g2[6]
 g2[2] != g3[6]
  g3[2] != g4[6]

g1[2] != g2[6]
g2[2] != g3[6]
 g3[2] != g4[6]

g2[2] != g3[6]
 g1[2] != g2[6]
g3[2] != g4[6]

g3[2] != g4[6]
 g2[2] != g3[6]
  g1[2] != g2[6]

1234
rlrl : 1번3번 r 2번4번 l
lrlr : 1번3번 l 2번4번 r

1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7
    *       *

2. 그걸 k번 수행한 뒤 점수 계산
1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
'''
import sys, collections
arr = [sys.stdin.readline().rstrip() for _ in range(4)]
g1 = collections.deque(arr[0])
g2 = collections.deque(arr[1])
g3 = collections.deque(arr[2])
g4 = collections.deque(arr[3])

k = int(sys.stdin.readline())

for i in range(k):
    num, dir = map(int, sys.stdin.readline().split())
    spin = [g1[2] != g2[6], g2[2] != g3[6], g3[2] != g4[6]]

    if num == 1:
        g1.rotate(dir)
        if spin[0]:
            g2.rotate(-dir)
            if spin[1]:
                g3.rotate(dir)
                if spin[2]:
                    g4.rotate(-dir)
    elif num == 2:
        g2.rotate(dir)
        if spin[0]:
            g1.rotate(-dir)
        if spin[1]:
            g3.rotate(-dir)
            if spin[2]:
                g4.rotate(dir)
    elif num == 3:
        g3.rotate(dir)
        if spin[1]:
            g2.rotate(-dir)
            if spin[0]:
                g1.rotate(dir)
        if spin[2]:
            g4.rotate(-dir)
    else :
        g4.rotate(dir)
        if spin[2]:
            g3.rotate(-dir)
            if spin[1]:
                g2.rotate(dir)
                if spin[0]:
                    g1.rotate(-dir)
score = 0
if g1[0] == '1' : score+=1
if g2[0] == '1' : score+=2
if g3[0] == '1' : score+=4
if g4[0] == '1' : score+=8

print(score)