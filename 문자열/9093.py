'''
단어 뒤집기

문장을 입력받고 각 단어를 뒤집어서 출력
2
I am happy today
We want to win the first prize
I ma yppah yadot
eW tnaw ot niw eht tsrif ezirp
'''
import sys
T = int(sys.stdin.readline())
for t in range(T):
    for arr in sys.stdin.readline().rstrip().split():
        for a in list(reversed(arr)):
            sys.stdout.write(a)
        sys.stdout.write(' ')