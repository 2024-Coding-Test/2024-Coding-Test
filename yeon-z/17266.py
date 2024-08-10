# 어두운 굴다리
import math
from sys import stdin
n = int(stdin.readline().strip()) # 굴다리 길이
m = int(stdin.readline().strip()) # 가로등 수
position = list(map(int, stdin.readline().strip().split()))

diff_max = -1
for i in range(len(position)-1):
    if position[i+1] - position[i] > diff_max:
        diff_max = position[i+1] - position[i]
# print(diff_max, position[0]-0, n - position[-1])
if diff_max == -1:
    print(n)
elif math.ceil(diff_max / 2)>= position[0] - 0 and math.ceil(diff_max / 2) >= n - position[-1]:
    print(math.ceil(diff_max / 2))
else:
    print( position[0] - 0 if position[0] - 0 > n - position[-1] else n - position[-1])