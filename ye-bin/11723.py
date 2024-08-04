from sys import stdin as s 

# input = sys.stdin.readline
# s = open("input.txt", 'rt')

S = set()
M = int(s.readline())

all_set = set(str(i) for i in range(1, 21))

for _ in range(M):
    order = s.readline().strip().split()
    
    # if order[0] == 'add' and order[1] not in S: # set은 중복 제거되므로 not in 조건 필요 없음
    if order[0] == 'add':
        S.add(order[1])
    elif order[0] == 'remove': # discard 사용해서 삭제하려는 요소가 집합 안에 없어도 오류가 나지 않도록 함
        S.discard(order[1])
    elif order[0] == 'check':
        print(1) if order[1] in S else print(0)
    elif order[0] == 'toggle':
        if order[1] in S:
            S.remove(order[1])
        else:
            S.add(order[1])
    elif order[0] == 'all':
        S = all_set.copy()
    else:
        S = set()