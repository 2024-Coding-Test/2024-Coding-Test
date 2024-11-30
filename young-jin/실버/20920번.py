import sys
input = sys.stdin.readline

n,m = map(int,input().split())
words = [input().strip() for _ in range(n)]

ans = []
word = {}

for w in words:
    if len(w) >= m:
        if w not in word:
            word[w] = 1
        else:
            word[w] += 1

for k,v in word.items():
    ans.append((k,v,len(k)))

sorted_ans = sorted(ans, key=lambda x: (-x[1], -x[2], x[0]))

for s in sorted_ans:
    print(s[0])