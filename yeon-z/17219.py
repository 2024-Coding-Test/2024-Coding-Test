# 비밀번호 찾기
from sys import stdin

M, N = map(int, stdin.readline().split())
dictionary = {}
for _ in range(M):
    web, password = map(str, stdin.readline().split())
    dictionary[web] = password

for _ in range(N):
    web = stdin.readline().strip()
    print(dictionary[web])