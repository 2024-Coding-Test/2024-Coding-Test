# 카펫
# 현재 코드
def solution(brown, yellow):
    answer = [3, 3]
    height = 0
    width = 1000000
    if yellow == 1:
        return answer
    for x in range(2, yellow + 1):
        if yellow % x == 0:
            y = yellow // x
            if abs(x - y) <= abs(width - height) and (x + 2) * (y + 2) == (brown + yellow):
                width = x
                height = y

    return [width + 2, height + 2]
# 이전 코드
def solution(brown, yellow):
    brown -= 4
    brown = brown // 2

    for i in range(1, brown):
        if i * (brown - i) == yellow:
            answer = [i + 2, brown - i + 2]
            answer.sort(reverse=True)
            return answer

    return answer