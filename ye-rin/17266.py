def is_light_sufficient(height, positions, N):
    current_position = 0
    for pos in positions:
        if pos - height > current_position:
            return False
        current_position = pos + height
    return current_position >= N

def find_minimum_height(N, positions):
    low, high = 0, N
    result = high
    
    while low <= high:
        mid = (low + high) // 2
        if is_light_sufficient(mid, positions, N):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


N = int(input().strip())    # 굴다리의 길이
M = int(input().strip())    # 가로등의 개수
positions = list(map(int, input().strip().split())) # M 개의 설치할 수 있는 가로등의 위치(오름차순, 중복 X, 정수)

minimum_height = find_minimum_height(N, positions)
print(minimum_height)   # 굴다리의 길이 N을 모두 비추기 위한 가로등의 최소 높이를 출력