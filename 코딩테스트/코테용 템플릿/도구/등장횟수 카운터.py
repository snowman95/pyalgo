'''
음수가 없는 배열에서
iterable 객체 각 요소의 등장횟수 카운트


'''
import collections
# 등장 횟수 많은 순서대로 dict(값:등장횟수) 반환
collections.Counter([1,2,3,1,2,3,3,4])
{3: 3, 1: 2, 2: 2, 4: 1}

# 등장 횟수 많은 순서대로 [tuple(값,등장횟수)] 반환
collections.Counter([1,2,3,1,2,3,3,4]).most_common()
[(3, 3), (1, 2), (2, 2), (4, 1)]

# 각 요소를 원하는 개수만큼 생성
[collections.Counter(a = 1, b = 2, c = 3).elements()]
[collections.Counter({'a':1, 'b':2, 'c':3}).elements()]
['a', 'b', 'b', 'c', 'c', 'c']

[collections.Counter({1:1, 2:2, 3:3}).elements()]
[1, 1, 2, 2, 3, 3, 3]


'''
배열에 음수가 포함된 경우
전체 배열에 아주 큰 수를 더해서 전부 양수로 바꿔서 적용하면 됨
'''