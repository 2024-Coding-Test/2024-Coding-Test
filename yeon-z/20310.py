# 타노스
from sys import stdin
import math

tanos = list(map(int, stdin.readline().strip()))
zero = math.ceil(tanos.count(0)/2)
one = math.ceil(tanos.count(1)/2)
result = []

leftOne = tanos.count(1)

for t in tanos:
    if t == 0 and zero:
        result.append(0)
        zero -= 1
    if t == 1:
        if leftOne <= one:
            result.append(1)
            one -= 1
        leftOne -= 1


print(''.join(map(str, result)))