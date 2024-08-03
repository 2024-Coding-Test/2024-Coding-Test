# 덩치

from sys import stdin

N = int(stdin.readline())
people = []
result = []

for _ in range(N):
    x, y = map(int, stdin.readline().strip().split())
    people.append([x, y])

for i in range(N):
    target = people[i]
    rank = 0
    for j in range(N):
        if i != j:
            if people[j][0] > target[0] and people[j][1] > target[1]:
                rank += 1
    result.append(rank+1)

print(' '.join(map(str, result)))