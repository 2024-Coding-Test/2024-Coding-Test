from sys import stdin

N = int(stdin.readline().strip())
maps = []
answer1 = 0 # 가로
answer2 = 0 # 세로

for _ in range(N):
    maps.append(list(stdin.readline().strip()))

for i in range(N):
    # 가로
    temp = 0
    for j in range(N):
        if maps[i][j] == '.':
            temp += 1
        else:
            if temp >= 2:
                answer1 += 1
                temp = 0
            else:
                temp = 0
    if temp >= 2:
        answer1 += 1

    # 세로
    temp = 0
    for j in range(N):
        if maps[j][i] == '.':
            temp += 1
        else:
            if temp >= 2:
                answer2 += 1
                temp = 0
            else:
                temp = 0
    if temp >= 2:
        answer2 += 1

print(answer1, answer2)