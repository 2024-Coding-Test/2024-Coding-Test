# 영단어 암기
# 1. 자주 나오는 단어일수록 앞에 배치
# 2. 해당 단어의 길이가 갈수록 앞에 배치한다.
# 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다.

from sys import stdin

N, M = map(int, stdin.readline().strip().split())
alphabet = {}
dict = []

for _ in range(N):
    alpha = stdin.readline().strip()
    if len(alpha) >= M:
        if alpha in alphabet:
            alphabet[alpha] += 1
        else:
            alphabet[alpha] = 1

for a in alphabet:
    dict.append([a, alphabet[a]])

# print(N, M)

dict.sort(key=lambda x: [-x[1], -len(x[0]), x[0]])
for d in dict:
    print(d[0])
# print(dict)
