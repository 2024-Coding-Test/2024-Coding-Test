# 현재 풀이
def solution(array, commands):
    result = []
    for c in commands:
        result.append(sorted(array[c[0] - 1: c[1]])[c[2] - 1])

    return result
# 이전 풀이
# def solution(array, commands):
#     answer = []
#     for c in commands:
#         tmp = array[c[0]-1:c[1]]
#         tmp.sort()
#         answer.append(tmp[c[2]-1])
#     return answer