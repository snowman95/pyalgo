import collections
q = collections.deque()
q.append()     #  □← 오른쪽 추가
q.popleft()    # ←□  왼쪽   빼기

q.appendleft() # →□  왼쪽   추가
q.pop()        #  □→ 오른쪽 빼기

# 값을 분리하여 추가하기 'defg' → 'd','e','f','g' 각각 추가
# append로 넣으면 'defg'로 들어가짐
q.extend()     #  □← 오른쪽 추가
collections.deque(['a','b','c']).extend('defg')
['a','b','c','d','e','f','g']

# n만큼 요소들을 회전시켜준다.
# n<0 : 왼쪽
# n>0 : 오른쪽
q.rotate(-1) # 왼
q.rotate(1)  # 오른