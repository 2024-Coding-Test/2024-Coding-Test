# 벌집
# 다시풀기 나중에 > 규칙을 왜 못 찾았지? ㅠ
# 기본 수학 규칙 찾는거

n = int(input())

result = 1
for i in range(n):
    result += i * 6

    if n <= result:
        print(i + 1)
        break