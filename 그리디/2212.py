'''
센서

센서 N개 - 1개 이상의 집중국과 통신가능해야함.
집중국 최대 K개 - 센서 수신기능영역 조절가능하며, 길이의 합 최소화해야함

원점
1 2 3 4 5 6 7 8 9
1   3     6 7   9
          6
    3(1)  6(4)

아이디어
1. 센서가 밀집되어 있는 집중국 설치한다.
무조건 센서 위치에 집중국 올려야 하는가?

1 2 3 4 5 6 7 8 9
1 2 3           9 
  * *      
6+9=15/2 = 7
센서 위치

가설 : 
어떤 센서 위에 집중국을 세워야한다.
가능하면 중앙에 위치한 센서 위에 세워야한다.
집중국이 여러개인 경우?

1 2 3 4 5 6 7 8 9
1 2 3           9 
    *
    *           *
  * *           *
* * *           *

먼가 규칙보이쥬?

1 2 3 4 5 6 7 8 9
1 2 3       7   9
    *
2 1 0       4   6
                *
2 1 0       2   0

arr[1]-arr[0]?????????????
1 1 4       2
1124


하나만 짓는다고 치자.
각 센서 위에 하나씩 지었을때 다른 센서까지의 거리합이 최소가 되는경우 채택
집중국에서 각 센서까지의 거리 표시하고

하나더 짓는다고 치자
각 센서 위에 하나씩 지었을때 (이미지어진 곳 제외) 거리합이 최소가 되는경우 채택
'''
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensors = sorted(list(map(int, sys.stdin.readline().split())))
diff = []

if k>=n:
    print(0)
else:
    for i in range(n-1):
        diff.append(sensors[i+1]-sensors[i])
    diff.sort(reverse=True)
    print(sum(diff[k-1:]))
    # 1 1 6
