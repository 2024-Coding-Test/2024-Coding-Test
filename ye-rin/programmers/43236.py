def solution(n, m, parking_lots):
    # 주차 구역 위치를 정렬합니다.
    parking_lots.sort()
    
    # 탐색 범위 초기화
    left = 1  # 최소 거리
    right = parking_lots[-1] - parking_lots[0]  # 최대 거리
    
    def can_place_parking_spots(distance):
        # 주어진 거리로 주차 구역을 배치할 수 있는지 확인합니다.
        count = 1  # 첫 번째 주차 구역은 항상 배치됩니다.
        last_position = parking_lots[0]
        
        for i in range(1, len(parking_lots)):
            if parking_lots[i] - last_position >= distance:
                count += 1
                last_position = parking_lots[i]
                if count >= m:
                    return True
        return False
    
    # 이진 탐색
    best_distance = 0
    
    while left <= right:
        mid = (left + right) // 2  # 중간 거리 계산
        
        if can_place_parking_spots(mid):
            best_distance = mid  # 현재 거리를 가능한 거리로 저장
            left = mid + 1  # 거리를 늘려서 탐색
        else:
            right = mid - 1  # 거리를 줄여서 탐색
    
    return best_distance