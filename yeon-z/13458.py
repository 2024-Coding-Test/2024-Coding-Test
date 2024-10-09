import math
N = int(input())
students = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0

for s in students:
    s -= B
    result += 1

    if s > 0:
        result += math.ceil(s / C)

print(result)

