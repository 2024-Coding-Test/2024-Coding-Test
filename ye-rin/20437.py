import sys

input = sys.stdin.readline

# 테스트 케이스 수 입력
t = int(input())

for _ in range(t):
    w = input().rstrip()  # 문자열 입력
    k = int(input())      # k 값 입력

    # 각 문자의 인덱스를 저장할 딕셔너리
    char_positions = {}
    
    # 문자열을 순회하면서 각 문자의 인덱스를 기록
    for i, char in enumerate(w):
        if char not in char_positions:
            char_positions[char] = []
        char_positions[char].append(i)
    
    # 결과 변수 초기화
    min_length = float('inf')  # 무한대로 초기화
    max_length = 0  # 0으로 초기화
    
    # 모든 문자의 인덱스 리스트를 순회
    for positions in char_positions.values():
        if len(positions) < k:
            continue  # k개 미만인 경우 무시
        
        # k개 이상인 문자의 인덱스 리스트를 슬라이딩 윈도우 방식으로 처리
        for i in range(len(positions) - k + 1):
            start_index = positions[i]
            end_index = positions[i + k - 1]
            length = end_index - start_index + 1
            
            # 최소, 최대 길이 업데이트
            min_length = min(min_length, length)
            max_length = max(max_length, length)
    
    # 결과 출력
    if min_length == float('inf'):
        print(-1)  # k개 문자를 포함하는 부분 문자열이 없는 경우
    else:
        print(min_length, max_length)  # 최소, 최대 길이 출력