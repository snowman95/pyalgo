import sys, string
new_id = "abcdefghijklmn.p"
new_id = new_id.lower()
arr = '0123456789-_.'
    
new_new_id = []
for s in new_id:
    if s in arr or s in string.ascii_lowercase:
        new_new_id.append(s)

new_id = ''.join(new_new_id)
while '..' in new_id:
    new_id = new_id.replace('..','.')
#4단계
if new_id and new_id[0] == '.':
    new_id = new_id[1:]
if new_id and new_id[-1] == '.':
    new_id = new_id[:-1]

#5단계
if not new_id:
    new_id = "a"
#6단계
if len(new_id) >= 16:
    new_id = new_id[:15]
    while new_id[-1] == '.':
        new_id = new_id[:-1]

if new_id:
    last_str = new_id[-1]
    size = 3-len(new_id)
    if size <= 2:
        new_id = new_id + last_str * size
print(new_id)