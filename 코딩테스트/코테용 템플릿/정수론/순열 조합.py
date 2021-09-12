import itertools

# 순열 (순서대로 나열)
data = ['A','B','C']
list(itertools.permutations(data,1))
[('A',), ('B',), ('C',)]
list(itertools.permutations(data,2))
[('A', 'B'), ('A', 'C'), 
('B', 'A'), ('B', 'C'), 
('C', 'A'), ('C', 'B')]
list(itertools.permutations(data,3))
[('A', 'B', 'C'), ('A', 'C', 'B'), 
('B', 'A', 'C'), ('B', 'C', 'A'), 
('C', 'A', 'B'), ('C', 'B', 'A')]

# 조합 (순서없이 뽑기)
data = ['A','B','C']
list(itertools.combinations(data,1))
[('A',), ('B',), ('C',)]
list(itertools.combinations(data,2))
[('A', 'B'), ('A', 'C'), ('B', 'C')]
list(itertools.combinations(data,3))
[('A', 'B', 'C')]

# 중복 순열 (중복선택 가능 순서대로 나열)
data = ['A','B','C']
list(itertools.product(data, repeat=1))
[('A',), ('B',), ('C',)]
list(itertools.product(data, repeat=2))
[('A', 'A'), ('A', 'B'), ('A', 'C'), 
('B', 'A'), ('B', 'B'), ('B', 'C'), 
('C', 'A'), ('C', 'B'), ('C', 'C')]
list(itertools.product(data, repeat=3))
[('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'A', 'C'), ('A', 'B', 'A'), ('A', 'B', 'B'), 
('A', 'B', 'C'), ('A', 'C', 'A'), ('A', 'C', 'B'), ('A', 'C', 'C'), ('B', 'A', 'A'), 
('B', 'A', 'B'), ('B', 'A', 'C'), ('B', 'B', 'A'), ('B', 'B', 'B'), ('B', 'B', 'C'), 
('B', 'C', 'A'), ('B', 'C', 'B'), ('B', 'C', 'C'), ('C', 'A', 'A'), ('C', 'A', 'B'), 
('C', 'A', 'C'), ('C', 'B', 'A'), ('C', 'B', 'B'), ('C', 'B', 'C'), ('C', 'C', 'A'), 
('C', 'C', 'B'), ('C', 'C', 'C')]

# 중복 조합 (중복선택 가능 순서없이 뽑기)
data = ['A','B','C']
list(itertools.combinations_with_replacement(data,1))
[('A',), ('B',), ('C',)]
list(itertools.combinations_with_replacement(data,2))
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
list(itertools.combinations_with_replacement(data,3))
[('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'A', 'C'), ('A', 'B', 'B'), ('A', 'B', 'C'), 
('A', 'C', 'C'), ('B', 'B', 'B'), ('B', 'B', 'C'), ('B', 'C', 'C'), ('C', 'C', 'C')]


'''
미리 조합을 만들어두고
집합으로 변환
'''
import itertools
def solution(relation):
    answer = 0
    # 전처리
    column_size = len(relation[0])
    arr = list(range(column_size))
    candidate_key = list()
    for cnt in arr:
        combi = list(itertools.combinations(arr, cnt+1))
        for col_num_arr in combi: # [(0,1) ... ]
            input = set(col_num_arr)
            valid = True
            for k in candidate_key:
                if k.issubset(input):
                    valid = False
                    break

            if not valid :
                continue
            box = []
            for row in relation: # [[...],[...]]
                tmp = []
                for col_num in col_num_arr: # (0,1)
                    tmp.append(row[col_num])
                box.append(''.join(tmp))
            if len(box) == len(set(box)):
                candidate_key.append(set(col_num_arr))
    answer = len(candidate_key)
    return answer

re = [
    ['a','1','aaa','c','ng'],
    ['b','1','bbb','c','g'],
    ['c','1','aaa','d','ng'],
    ['d','2','bbb','d','ng']]
solution(re)