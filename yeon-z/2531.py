# 회전초밥
# 초밥의 종류 번호로 표현
# 벨트 위에는 같은 종류의 초밥이 둘 이상 있을 수 있다.

# 1. 원래 회전 초밥은 손님이 마음대로 초밥을 고르고, 먹은 초밥만큼 식대를 계산하지만, 벨트의 임의의 한 위치부터 K개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공
# 2. 각 고객에게 초밥의 종류 하나가 쓰인 쿠폰을 발행하고, 1번 행사에 참가할 경우 이 쿠폰에 적혀진 종류의 초밥 하나를 추가로 무료로 제공한다.
# 만약 이 번호에 적혀진 초밥이 현재 벨트 위에 없을 경우, 요리사가 새로 만들어 손님에게 제공한다.

# 초밥 벨트에서 최대로 먹을 수 있는 초밥 종류

from sys import stdin
from collections import defaultdict

# n 벨트 위 접시 수
# d 초밥 가짓 수
# k 연속해서 먹는 접시의 수
# c 쿠폰 번호
n, d, k, c = map(int, stdin.readline().strip().split())
belt = [int(stdin.readline()) for _ in range(n)]

# 초밥 종류 카운트
sushi_counter = defaultdict(int)

# 초기 슬라이딩 윈도우 설정
for i in range(k):
    sushi_counter[belt[i]] += 1

# 쿠폰 초밥 추가
sushi_counter[c] += 1

# 출력값:: 최대 종류 수
result = len(sushi_counter)

for i in range(1, n):
    # 슬라이딩 왼쪽 초밥 제거
    sushi_counter[belt[i - 1]] -= 1
    if sushi_counter[belt[i - 1]] < 1:
        del sushi_counter[belt[i - 1]]
    # 오른쪽 초밥 추가
    sushi_counter[belt[(i + k - 1) % n]] += 1

    result = max(result, len(sushi_counter))

print(result)