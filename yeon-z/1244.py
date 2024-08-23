# 스위치 켜고 끄기
# 1부터 연속적으로 번호 스위치
# 스위치 on or off
# 1 on , 0 off
# 성별과 받은 수에 따라 스위치 조작
# 남학생 스위치 번호가 자기가 받은 수의 배수면 스위치 상태 변경
# 여학생 받은수와 같은 번호의 스위치를 중심으로 좌우가 대칭이면 가장 많은 스위치를 포함하는 구간을 찾아서 그 구간에 속하는 스위치 상태를 모두 바꿈
# 남학생 1, 여학생 2
# ex) 스위치 상태 0 1 1 1 0 1 0 1
# 여학생이 받은 번호 3
# 0 1 1 1 0 대칭 > 1 0 0 0 1 로 변경

# 예시
# 0 1 0 1 0 0 0 1
# 1 3
# 2 3

# 1 3 > 0 1 1 1 0 1 0 1
# 2 3 > 1 0 0 0 1 1 0 1

from sys import stdin

N = int(stdin.readline())
switch = [-1]
switch.extend(list(map(int, stdin.readline().strip().split())))

T = int(stdin.readline())

for _ in range(T):
    sex, number = map(int, stdin.readline().strip().split())
    if sex == 1:
        # 남학생
        target = [i for i in range(1, N+1) if i % number == 0]
        for t in target:
            switch[t] = 1 if switch[t] == 0 else 0
    else:
        # 여학생
        lr = 1
        while number - lr >= 1 and number + lr <= N:
            left = number - lr
            right = number + lr
            if switch[left] == switch[right]:
                lr += 1
            else:
                break
        lr -= 1
        target = switch[number-lr: number+lr+1]

        for idx in range(number-lr, number+lr+1):
            switch[idx] = 1 if switch[idx] == 0 else 0

switch = switch[1:]
for i in range(0, N, 20):
    print(' '.join(map(str, switch[i: i+20])))
