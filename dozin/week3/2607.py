n=int(input())
words=[
    input()
    for _ in range(n)
]

cnt=0
for i in range(len(words)):
    if words[i]==words[0]:
        break
    if (set(words[i]) == set(words[0])):
        cnt+=1

print(cnt)