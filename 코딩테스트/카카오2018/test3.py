'''
후보키

유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 "유일"하게 식별되어야 한다.
최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다. 
즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.

위 두개의 조건을 만족하는 후보 키의 최대 개수를 구하라.

1. 단일) 각 column 마다 모든 row가 유일하면 ok
2. 여러) 두개 이상의 column 합쳤을때 유일하면 ok

최소성이란, A+B로도 충분한데 굳이 A+B+C 안해도 된다는 것.
A+B, B+C, A+C 셋 중 하나라도 만족하면 A+B+C는 후보키 아님!!!

column 1~8
row 1~20
문자열길이 1~8

이거 8개면, 모든 조합 만들어보면될듯?

[[row1],[row2]...[row n]] 이렇게 들어옴.
len([row1]) -> 전체 컬럼 수

아이디어
1. 조합가능한 수 확인한다.
1개조합
2개조합
..
이렇게 늘려나감 - 근데 이렇게 하면 너무 많으니 가지쳐야함
이렇게 하자,

n개의 조합 만드는데 후보키 나오면 그거 제외하고 진행한다.
ex) A -> 이제 A 빼고 B,C,D로만 진행

A+B가 후보키면? 흠 이거 bfs냐?
bfs로 해도 될듯?
key 조합 [1,2,3] 이렇게 큐에 넣고
뺐을때 그게 유일한지만 확인하면 되잖아? -> 어떻게 보면 쿼리 문제임. 

[아이디어 정리]
1. 사전에 모든 조합을 만들어서 배열에 넣어둔다.
2. BFS를 돌면서 [1,2,3] 이런식으로.. 선택되지 않은것 진행함.


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
#[["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
#re = [["a", "1"], ["a", "bc"], ["x", "yz"], ["x", "c"]]
#[["100","100","ryan","music","2"], ["200","200","apeach","math","2"], ["300","300","tube","computer","3"], ["400","400","con","computer","4"], ["500","500","muzi","music","3"], ["600","600","apeach","music","2"]]#[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
solution(re)