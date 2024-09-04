# 모음 사전
def solution(word):
    answer = 0
    dict = {
        'A': 1,
        'E': 2,
        'I': 3,
        'O': 4,
        'U': 5
    }
    n = len(word)
    word = list(word)[::-1]
    for index, value in enumerate(word):
        index += 5 - (n)
        if value == 'A':
            answer += 1
            pass
        else:
            cal = 0
            for i in range(index+1):
                cal += pow(5, i)
            answer += cal * (dict[value] - 1) + 1
    return answer