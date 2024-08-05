# 임스와 함께하는 미니게임 성공

from sys import stdin

n, game = map(str, stdin.readline().split())
people = set([])

for _ in range(int(n)):
    people.add(stdin.readline().strip())

if game == 'Y':
    print((len(people)))
elif game == 'F':
    print(len(people) // 2)
else:
    print(len(people) // 3)
