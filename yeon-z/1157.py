from sys import stdin

s = list(stdin.readline().strip().upper())
sSet = set(s)

word = ['']
count = 0

for idx, _s in enumerate(sSet):
    cnt = s.count(_s)
    if cnt > count:
        count = cnt
        word = [_s]
    elif cnt == count:
        word.append(_s)

if len(word) == 1:
    print(word[0])
else:
    print('?')