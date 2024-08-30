# 가장 큰 수
# 현재 코드
def solution(numbers):
    numbers = [str(n) for n in numbers]
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    numbers = ''.join(numbers)
    return '0' if int(numbers) == 0 else numbers

# 이전 코드
def solution(numbers):
    answer = [0 for _ in range(len(numbers))]
    for n in range(len(numbers)):
        answer[n] = (str(numbers[n]) * 3) + '-' + str(numbers[n])

    answer.sort(reverse=True)
    for i in range(len(answer)):
        answer[i] = answer[i][answer[i].index('-') + 1:]
    answer = ''.join(answer)
    return '0' if int(answer) == 0 else answer