import sys,collections,string
s = sys.stdin.readline().rstrip()
arr = {}
for i in string.ascii_lowercase:
    arr[i] = 0
for key,value in dict(collections.Counter(s)).items():
    arr[key] = value
for i in string.ascii_lowercase:
    sys.stdout.write(str(arr[i]) + ' ')