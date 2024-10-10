# 정수 삼각형
def solution(triangle):
    triangle = triangle[::-1]

    prev = triangle[0]
    for i in range(1, len(triangle)):
        prev2 = []
        for j in range(len(triangle[i])):
            temp = []
            temp.append(prev[j] + triangle[i][j])
            temp.append(prev[j + 1] + triangle[i][j])
            prev2.append(max(temp))
        prev = prev2
    return prev[0]