'''
누적합

[1, 2, 3, 4, 5] 를
[1, 1+2, 1+2+3, 1+2+3+4, 1+2+3+4+5] 로 반환
'''
import itertools
list(itertools.accumulate([1,2,3,4,5]))
[1, 3, 6, 10, 15]