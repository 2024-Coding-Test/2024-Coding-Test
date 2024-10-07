import sys
input = sys.stdin.readline

# 두 도시 x와 y를 같은 집합으로 합치기
def union(x, y):
    x = find(x)  # x의 루트 부모 찾기
    y = find(y)  # y의 루트 부모 찾기
    # 두 루트 부모를 비교하여 더 작은 값을 부모로 설정
    if x < y:
        parents[y] = x  # y의 부모를 x로 설정
    else:
        parents[x] = y  # x의 부모를 y로 설정
    
# 주어진 도시 x의 루트 부모 찾기
def find(x):
    if x != parents[x]:  # x가 자신의 부모가 아닌 경우
        parents[x] = find(parents[x])  # 경로 압축을 통해 루트 부모 찾기
    return parents[x]  # x의 최상위 부모 반환

# 유니온-파인드 초기화
n, m = int(input()), int(input())  # 도시의 개수(n)와 여행 계획에 포함된 도시의 개수(m) 입력
parents = [i for i in range(n)]  # 각 도시의 부모를 초기화 (자기 자신을 부모로 설정)

# 도로 정보 입력 및 유니온 처리
for i in range(n):  # n개의 도시에 대해
    link = list(map(int, input().split()))  # 연결된 도로 정보를 입력받음
    for j in range(n):  # 각 도시와 연결된 도로를 확인
        if link[j] == 1:  # 도시 i와 도시 j가 연결되어 있을 경우
            union(i, j)  # 두 도시를 같은 집합으로 합침

# 여행 계획의 경로 체크
parents = [-1] + parents  # 인덱스를 1부터 사용하기 위해 -1로 패딩
path = list(map(int, input().split()))  # 여행 계획에 포함된 도시 리스트 입력
start = parents[path[0]]  # 여행 계획의 첫 번째 도시의 부모를 기준으로 설정

# 여행 계획에 있는 모든 도시가 같은 집합에 있는지 확인
for i in range(1, m):  # 여행 계획의 도시들을 순회
    if parents[path[i]] != start:  # 현재 도시의 부모가 시작 도시의 부모와 다르면
        print("NO")  # 서로 다른 집합이므로 여행 불가능
        break
else:
    print("YES")  # 모두 같은 집합이면 "YES" 출력