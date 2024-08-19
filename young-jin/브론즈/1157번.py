from collections import Counter

word = list(input().upper())

count = Counter(word)

answer = []
for w in count:
    if count[w] == max(count.values()):
        answer.append(w)

if len(answer) == 1:
    print(answer[0])
else:
    print('?')