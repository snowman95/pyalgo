
s = set()
other = set()
others = set()

s.isdisjoint(other) # 집합이 other 와 공통 원소를 갖지 않는 경우(교집합=공집합) True
s.issubset(other)
set <= other      # 집합의 모든 원소가 other 에 포함되는지 검사합니다.
set < other       # 집합이 other 의 진부분집합인지 검사 set <= other and set != other.

s.issuperset(other)
set >= other      # other 의 모든 원소가 집합에 포함되는지 검사합니다.
set > other       # 집합이 other 의 진상위집합인지 검사 set >= other and set != other.

s.union(*others)
set | other | ... # 집합과 others의 합집합 반환

s.intersection(*others)
set & other & ... # 집합과 others의 교집합 반환

s.difference(*others)
set - other - ... # 집합과 others의 차집합 반환

s.symmetric_difference(other)
set ^ other       # 집합이나 other에 포함되어 있으나 교집합이 아닌것 반환

s.update(*others)
set |= other      # 집합을 갱신해서, 모든 others의 원소들을 더합니다.

s.intersection_update(*others)
set &= other       # 집합을 갱신해서, 교집합만 남김

s.difference_update(*others)
set -= other       # 집합을 갱신해서, others에 있는 원소들을 제거합니다.

s.symmetric_difference_update(other)
set ^= other       # 집합을 갱신해서, 두 집합의 어느 한 곳에만 포함된 원소들만 남깁니다.

s.add(elem)        # 원소 elem 을 집합에 추가.
s.remove(elem)     # 원소 elem 을 집합에서 제거. elem 가 집합에 없다면 KeyError 발생.
s.discard(elem)    # 원소 elem 이 집합에 포함되어 있으면 제거
s.pop()            # 집합으로부터 임의의 원소를 제거해 반환. 공집합이면 KeyError 발생
s.clear()          # 집합의 모든 원소를 제거