# 카드 2
# 1번 부터 2번의 카드가 존재
# N번 카드가 가장 아래, 1번 카드가 가장 위 시작

# 1. 제일 위에 있는 카드 버림
# 2. 제일 위에 있는 카드를 제일 아래 카드 밑으로 옮김
# ex) N= 4
# 1 2 3 4
# 2 3 4
# 3 4 2
# 4 2
# 2 4
# 4

from sys import stdin
from collections import deque

N = int(stdin.readline())
queue = deque([i + 1 for i in range(N)])

while len(queue) > 1:
    queue.popleft()
    temp = queue.popleft()
    queue.append(temp)
print(queue[0])