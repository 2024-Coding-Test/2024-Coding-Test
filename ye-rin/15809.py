import sys

# 국가 수 (N)와 명령의 수 (M) 입력
N, M = map(int, sys.stdin.readline().split())

# 국가 병력을 저장하는 리스트 초기화 (1번부터 시작하기 위해 0번째 인덱스는 0으로 채움)
conturies = [0]
for _ in range(N):
    conturies.append(int(sys.stdin.readline()))  # 각 국가의 병력을 입력받아 추가

# 유니온-파인드에서 루트 노드를 찾는 함수
def find(n):
    now = conturies[n]  # 현재 노드의 병력 정보 또는 루트 노드 정보
    if now < 0:
        # 현재 노드가 루트가 아니라면, 루트 노드를 재귀적으로 찾아 반환
        return find(-1 * now)
    else:
        # 루트 노드인 경우 자신의 인덱스를 반환
        return n

# 각 명령을 처리
for _ in range(M):
    # 명령 타입 (com), 국가 x, 국가 y를 입력받음
    com, x, y = map(int, sys.stdin.readline().split())
    
    # x와 y의 루트 노드를 찾음
    find_x = find(x)
    find_y = find(y)

    if com == 1:
        # 동맹 명령 (com == 1)
        # 두 국가가 서로 동맹을 맺을 때
        conturies[find_x] += conturies[find_y]  # x의 루트 노드에 y의 병력을 추가
        conturies[find_y] = -1 * find_x         # y의 루트 노드를 x의 루트로 설정 (연결)

    else:
        # 전쟁 명령 (com == 2)
        # 병력이 같다면 두 국가 모두 병력이 소멸
        if conturies[find_x] == conturies[find_y]:
            conturies[find_x] = 0
            conturies[find_y] = 0
        # x의 병력이 더 많은 경우
        elif conturies[find_x] > conturies[find_y]:
            conturies[find_x] -= conturies[find_y]  # x의 병력에서 y의 병력을 뺌
            conturies[find_y] = -1 * find_x         # y의 루트를 x로 설정
        # y의 병력이 더 많은 경우
        else:
            conturies[find_y] -= conturies[find_x]  # y의 병력에서 x의 병력을 뺌
            conturies[find_x] = -1 * find_y         # x의 루트를 y로 설정

# 병력이 남은 국가들만 결과 리스트에 추가
answer = []
for i in conturies:
    if i > 0:  # 양수인 경우 병력이 남아 있는 국가
        answer.append(i)

answer.sort()  # 병력을 정렬하여 출력
print(len(answer))  # 병력이 남아 있는 국가 수 출력
print(*answer)  # 각 국가의 병력 출력