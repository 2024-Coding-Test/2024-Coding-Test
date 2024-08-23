# 비슷한 단어
# 두 단어가 같은 구성을 갖는 경우
# 한 단어에 문자를 더하거나, 빼거나 하나의 문자를 다른 문자로 바꾸어 나무저 한 단어와 같은 구성을 갖게되는 경우
# 입력으로 주어진 첫 번째 단어아 비슷한 단어의 수

from sys import stdin

N = int(stdin.readline())
target = list(stdin.readline().strip())
result = 0

for _ in range(N-1):
    case = stdin.readline().strip()
    compare = target[:]
    cnt = 0

    for c in case:
        if c in compare:
            compare.remove(c)
        else:
            cnt += 1
    if len(compare) < 2 and cnt < 2:
        result += 1
print(result)