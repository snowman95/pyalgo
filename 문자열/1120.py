'''
문자열

길이가 N인 문자열 X,Y
X와 Y차이는 같은 인덱스 위치가 다른값의 개수

A길이 <= B길이 인 문자열 A,B
A가 B와 길이 같아질 때까지 A의 앞/뒤에 아무 알파벳 추가 가능하다.
A,B 길이 같게 만들었을때의 최소 차이

아이디어
adaabc → aababbc

adaabc
aababbc

이거좀 이해가 안되는데
처음에 가장 비슷하게 맞춰놓고 그냥 안맞는 개수만큼 더하면 끝아님?

diff = len(A)-len(B)
max_cnt = 0
for i in range(diff):
    1칸씩 옆으로 밀면서 가장 똑같아지는 경우 찾아라
    cnt = 0
    for j in range(len_a): a의 길이만큼 확인
        if arr_b[i+j] == arr_a[j]:
            cnt+=1
    if max_cnt < cnt:
        max_cnt = cnt
'''
import sys
arr_a,arr_b = sys.stdin.readline().split()
len_a = len(arr_a)
len_b = len(arr_b)
max_cnt = 0
for i in range(len_b-len_a+1):
    cnt = 0
    for j in range(len(arr_a)):
        if arr_b[i+j] == arr_a[j]: cnt+=1
    max_cnt= max(max_cnt,cnt)
print(len_a-max_cnt)