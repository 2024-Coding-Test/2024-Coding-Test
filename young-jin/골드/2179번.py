import sys
input = sys.stdin.readline

n = int(input())
words = []
for _ in range(n):
    words.append(input().strip())
tmp = set()

sorted_words = sorted(words)

M = 0; m = 0
for i in range(n-1):
    if sorted_words[i][0] != sorted_words[i+1][0]:
        continue
    
    l = max(len(sorted_words[i]), len(sorted_words[i+1]))
    for j in range(1,l+1):
        if sorted_words[i][:j] != sorted_words[i+1][:j]:
            break
        else:
            pre = sorted_words[i][:j]
            m = j
    
    if M <= m:
        M = m
        tmp.add((words.index(sorted_words[i]),sorted_words[i], pre, m))
        tmp.add((words.index(sorted_words[i+1]),sorted_words[i+1], pre, m))

ans = []
for t in tmp:
    _,_,_,count = t
    if count >= M:
        ans.append(t)

ans = sorted(ans, key = lambda x : x[0])

print(ans[0][1])

for i in range(1,len(ans)):
    if ans[0][2] == ans[i][2]:
        print(ans[i][1])
        break