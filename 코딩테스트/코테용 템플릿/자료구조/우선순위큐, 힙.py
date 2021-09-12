'''
heappush(heqp, (a,b))
(a,b)  : a(오름↗) → b(오름↗) 정렬
(b,a)  : b(오름↗) → a(오름↗) 정렬
(a,-b)
(-a,b) : a(내림↘) → b(오름↗) 정렬  (pop하고 -a 해야함)
(-a,-b): a(내림↘) → b(내림↘) 정렬  (pop하고 -a -b해야함)
(-b,a) : b(내림↘) → b(오름↗) 정렬  (pop하고 -b 해야함)
(-b,a) : b(내림↘) → b(오름↗) 정렬  (pop하고 -b 해야함)
(-b,-a): b(내림↘) → b(내림↘) 정렬  (pop하고 -a -b 해야함)


# 최소 힙
heap = [] : 리스트
heapq.heappush(heap, (a, b)) : 힙에 하나 추가 O(logN)
a = heapq.heappop(heap)    : 힙에서 하나 빼서 반환 O(logN)
heap[0] : 힙에서 빼지않고 값 얻기 O(1)

이미 값이 있는 리스트를 힙으로 사용하려면 변환이 필요
heapq.heapify(heap)        : 변환 (리스트 → 힙) O(N)



# 최대 힙
heap = [] : 리스트
heapq.heappush(heap, (-a, b)) : 힙에 하나 추가 O(logN)
a = heapq.heappop(heap)[1]    : 힙에서 하나 빼서 반환 O(logN)
heap[0][1]                    : 힙에서 빼지않고 값 얻기 O(1)

이미 값이 있는 리스트를 힙으로 사용하려면 변환이 필요
heapq.heapify_max(heap)        : 변환 (리스트 → 힙) O(N)



a = heapq.heappushpop(heap, 원소) : 힙에 하나 추가하고 하나 빼서 반환
(heappush() → heappop() 순서로 호출하는 것 보다 효율적)
a = heapq.heapreplace(heap, 원소) : 힙에서 하나 빼서 반환 후 하나 추가
(heappop() → heappush() 순서로 호출하는 것 보다 효율적)

a = heapq.nlargest(n, heap, key=None) : n개의 가장 큰 요소로 구성된 리스트 반환
a = heapq.nsmallest(n, heap, key=None) : n개의 가장 작은 요소로 구성된 리스트 반환
key=요소 비교에 사용되는 함수 (n이 너무크면 sorted가 효율적임)


'''