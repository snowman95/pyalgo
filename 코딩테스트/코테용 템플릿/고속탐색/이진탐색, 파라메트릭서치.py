'''
직접 구현 방법
'''
def binary_serach(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        # mid에 해당하는 값이 target이면 종료
        if arr[mid] == target:
            return mid
        # mid에 해당하는 값이 target보다 크면 
        # mid 빼고 앞으로 탐색
        elif arr[mid] > target:
            end = mid - 1
        # mid에 해당하는 값이 target보다 작으면
        # mid 빼고 뒤로 탐색
        else:
            start = mid + 1
    return None
'''
파라메트릭 서치
이진탐색하며 중간값으로 잘랐을때 어떤 조건을 만족하는지 확인

1. 바이너리 서치 진행
2. 전체 배열값 - mid = 잘라낸 윗꼭다리 전체합
   (mid가 커질수록 꼭다리 전체합은 줄어든다.)
3. 이 꼭다리들의 합이 m보다 큰것중에 최대 mid값 구해라

ex) mid가 1,2,3 이렇게 잘라도 꼭다리 합이 m보다 큰데
여기서 젤큰 3을 골라야되는거임.
'''
import sys
n,m = map(int,sys.stdin.readline().split())
target = list(map(int,sys.stdin.readline().split()))
start = 0
end = 2**31-1 # end값은 겁나 커도 상관없음.
while start <= end:
    mid = (start+end)//2
    cnt = 0
    # 전체 배열값 - mid = 잘라낸 윗꼭다리합
    for item in target:
        if item > mid:
            cnt += item-mid
    # 꼭다리 합이 m보다 크면 end고정
    # start값을 뒤로당기면서 더 높은 높이로 잘라봄
    if m <= cnt:
        start = mid+1
    # 꼭다리 합이 m보다 작으면 start고정
    # end값을 앞으로당기면서 더 작은 높이로 잘라봄
    else:
        end = mid-1
print(end)