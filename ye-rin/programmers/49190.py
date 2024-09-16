def solution(arrows):
    # 이동 방향을 정의
    # 0: 위, 1: 오른쪽 위, 2: 오른쪽, 3: 오른쪽 아래, 4: 아래, 5: 왼쪽 아래, 6: 왼쪽, 7: 왼쪽 위
    move = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
    
    # 기록된 선을 저장할 리스트
    edge = []
    # 시작점을 포함한 정점의 목록
    vertex = [(0,0)]
    # 방의 개수를 저장할 변수
    room = 0
    
    # 주어진 방향에 따라 이동
    for i in arrows:
        # 각 방향에 대해 두 번 이동
        for j in range(1, 3):
            # 현재 위치를 추적
            current = vertex[-1]
            # 이동할 새로운 좌표를 계산
            a, b = current[0] + move[i][0], current[1] + move[i][1]
            
            # 새로운 좌표가 기존의 정점 목록에 있는지 확인
            if (a, b) in vertex:
                # 선이 이미 기록된 경우, 방을 인식하지 않고 넘어감
                if (current[0], current[1], a, b) in edge or (a, b, current[0], current[1]) in edge:
                    edge.append((current[0], current[1], a, b))
                    vertex.append((a, b))                   
                    continue
                else:
                    # 새로운 방이 발견된 경우
                    edge.append((current[0], current[1], a, b))
                    vertex.append((a, b))
                    room += 1
                    continue
            # 새로운 선을 기록하고 정점 목록에 추가
            edge.append((current[0], current[1], a, b))
            vertex.append((a, b))

    # 최종 방의 개수를 반환
    return room