# 조이스틱
# 조이스틱
def solution(name):
    A = 65
    Z = 90
    answer = 0
    n = len(name)

    # 각 문자에 대해 위아래 조작 횟수 계산
    for char in name:
        answer += min(ord(char) - A, Z - ord(char) + 1)

    # 좌우 이동 최소값 계산
    move = n - 1
    for i in range(n):
        next = i + 1
        while next < n and name[next] == 'A':
            next += 1
        move = min([move, 2 * i + n - next, i + 2 * (n - next)])

    return answer + move