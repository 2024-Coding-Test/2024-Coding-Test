# 줄세우기
# 키 순서대로 번호를 부여
# 가장 작은 아이 1번, 2번, ...
# 반 아이들 항상 20명
# 같은 키 한명도 없음
# 우선 아무나 한 명을 뽑아 줄의 맨 앞에 세운다.
# 학생이 한 명씩 줄의 맨 뒤에 서면서 다음 과정을 거친다.
# - 자기 앞에 자기보다 키가 큰 학생이 없다면 그냥 그 자리에 서고 차례가 끝난다.
# - 자기 앞에 자기보다 키가 큰 학생이 한 명 이상 있다면 그 중 가장 앞에 있는 학생 (A)의 바로 앞에 선다. 이때 A부터 그 뒤의 모든 학생들은 공간을 만들기 위해 한 발씩 뒤로 물러서게 된다.

# 오름차순 줄 서기
# 총 몇번 뒤로 물러서게 되누?

from sys import stdin
n = int(stdin.readline().strip())
for _ in range(n):
    inputList = list(map(int, stdin.readline().strip().split()))
    idx = inputList[0]
    student = inputList[1:]
    result = 0

    for i in range(1, 20):
        left = student[:i]

        tempIdx = -1
        for j in range(len(left)-1, -1, -1):
            if left[j] > student[i]:
                tempIdx = j
                result += 1
        if tempIdx > -1:
            temp = student[tempIdx]
            student[tempIdx] = student[i]
            student[i] = temp
    print(str(idx) + ' ' + str(result))