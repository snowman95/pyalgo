'''
접미사 배열
'''
import sys
s = sys.stdin.readline().rstrip()
result = []
for start in range(len(s)):
    result.append(s[start:])
for item in sorted(result):
    print(item)