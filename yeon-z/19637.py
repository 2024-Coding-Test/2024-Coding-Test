# IF문좀 대신 써줘
from sys import stdin

N, M = map(int, stdin.readline().strip().split())

powers = []

for _ in range(N):
    # 전투력
    n, p = map(str, stdin.readline().strip().split())
    powers.append([n, p])

powers.sort(key=lambda x: int(x[1]))

for _ in range(M):
    # 캐릭터 전투력 입력 받기
    p = int(stdin.readline().strip())
    left = 0
    right = len(powers)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if int(powers[mid][1]) >= p:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    print(powers[result][0])