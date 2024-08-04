from sys import stdin as s 

s = open("input.txt", "rt")

# 처음에 풀던 방식
# N = int(s.readline())
# left_cnt = list(map(int, s.readline().strip().split())) # 왼쪽 사람 수
# result = [0 for i in range(N)] # 줄을 선 순서

# # 키 작은 순으로 줄서기
# for i in range(1, N+1):
#     cnt = 0 # 왼쪽에 있는 키 큰 사람 카운트
    
#     # 왼쪽에 최소 있어야 하는 사람 수 자리만큼 건너뛰고 줄서기 시작
#     for j in range(left_cnt[i-1], N):
#         if result[j] == 0: # 만약 해당 자리가 비어있다면 거기에 줄서기
#             result[j] = i
#             break
#         else: # 자리가 이미 차있다면 앞에서부터 자기보다 큰 사람 수 + 빈 자리 수 = left_cnt 같아지는 자리 찾기
#             for k in range(N-1):
#                 if result[k] > i or result[k] == 0:
#                     cnt += 1 
#                 if cnt == left_cnt[i-1]:
#                     if result[k+1] == 0:
#                         result[k+1] = i
#                         break 
#                     else:
#                         continue
#             break

# print(' '.join(map(str, result)))

# N명의 사람 수와 각 사람의 왼쪽에 있어야 하는 큰 사람 수를 입력 받는다.
N = int(s.readline())
left_cnt = list(map(int, s.readline().strip().split())) # 왼쪽 사람 수
result = [0] * N

# 키가 작은 사람부터 시작하여, 각 사람이 적절한 자리에 배치될 수 있도록 한다.
for i in range(1, N+1):
    count = left_cnt[i-1]  # i번째 사람이 왼쪽에 있어야 하는 큰 사람 수
    
    for j in range(N):
        # 키가 작은 사람부터 줄서기 때문에 자리가 채워져있다면 무조건 나보다 키가 작은 사람임
        # 현재 자리가 비어있고, 남아있는 큰 사람의 수가 0일 때, 자리에 배치한다.
        if result[j] == 0 and count == 0:
            result[j] = i
            break
        elif result[j] == 0:
            # 현재 자리가 비어있다면, 큰 사람의 수를 감소시킨다.
            count -= 1

# 결과를 출력한다.
print(' '.join(map(str, result)))