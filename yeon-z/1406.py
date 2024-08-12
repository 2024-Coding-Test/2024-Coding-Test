# 에디터
# L: 커서 왼쪽으로 한칸
# D: 커서 오른쪽으로 한칸
# B: 커서 왼쪽에 있는 문자를 삭제
# P $ : $ 라는 문자를 커서 왼쪽에 추가함

from sys import stdin

left = list(stdin.readline().strip())
N = int(stdin.readline())
right = []

for _ in range(N):
    command = stdin.readline().strip().split()
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

left.extend(right[::-1])
print(''.join(left))