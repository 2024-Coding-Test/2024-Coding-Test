import sys
input = sys.stdin.readline

word = input().strip()

count = {'a' : 0, 'b' : 0}
for w in word:
    count[w] += 1

k = count['a']
n = len(word)

ans = 1e9
for i in range(n):
    if i+k <= n:
        window = word[i:i+k]
    else:
        window = list(word[i:] + word[:(i+k)%n])

    count = {'a' : 0, 'b' : 0}
    for w in window:
        count[w] += 1

    ans = min(ans, count['b'])

print(ans)