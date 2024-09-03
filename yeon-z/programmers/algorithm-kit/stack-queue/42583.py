# 다리를 지나는 트럭
# 현재 코드
from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    answer = 0
    time = deque([])
    bridge = deque([])

    while len(bridge) > 0 or len(truck_weights) > 0:
        answer += 1
        # 다리 위에 있는 놈들 이동해라
        for i in range(len(time)):
            time[i] += 1

        if len(time) > 0 and time[0] >= bridge_length:
            time.popleft()
            bridge.popleft()

        # 현재 다리위에 있는 트럭들의 무게 + 다음 건널 예정인 트럭 무게 합이 다리가 버티는 무게보다 작거나 같은 경우만 다리위에 올라감
        if len(bridge) > 0 and len(truck_weights) > 0:
            if (sum(bridge) + truck_weights[0]) <= weight:
                bridge.append(truck_weights.popleft())
                time.append(0)
        elif len(bridge) == 0 and len(truck_weights) > 0:
            bridge.append(truck_weights.popleft())
            time.append(0)

    return answer

# 이전 코드
from collections import deque
def solution(bridge_length, weight, truck_weights):
    max_count = bridge_length
    max_weight = weight

    time = 0
    n = len(truck_weights)

    Complete = deque()
    Progress = deque()
    Wait = deque(truck_weights)

    while len(Complete) < n:
        time += 1
        if len(Progress) > 0:
            for idx in range(len(Progress)):
                Progress[idx][0] -= 1
            if Progress[0][0] == 0:
                Complete.append(Progress.popleft())

        if len(Wait) > 0:
            _sum = sum(sub_arr[1] for sub_arr in Progress)
            if len(Progress) < max_count and _sum + Wait[0] <= max_weight:
                Progress.append([max_count, Wait.popleft()])

    return time