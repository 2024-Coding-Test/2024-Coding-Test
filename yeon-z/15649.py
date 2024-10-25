# N과 M(1)
from itertools import permutations

N, M = map(int, input().split())

arr = [i + 1 for i in range(N)]

result = list(permutations(arr, M))
result.sort()

for r in result:
    print(' '.join(map(str,r)))