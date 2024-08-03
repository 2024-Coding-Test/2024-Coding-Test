# 한 줄 서기
# 사람들은 자기보다 큰 사람이 왼쪽에 몇 명 있었는지만을 기억
# N명의 사람이 있고, 사람들의 키는 1부터 N까지 모두 다르다

from sys import stdin

N = int(stdin.readline())
numbers = list(map(int, stdin.readline().strip().split()))
result = [0 for _ in range(N)]

for idx, n in enumerate(numbers):
    # 1. 나보다 큰 사람이 몇명 남았는지 확인하고 배치해야 한다.
    # 2. 기준이 되는 n의 왼쪽 큰 사람 수가 3이라고 할때 앞에 빈칸이 3개있는 다음에 빈 자리가 n의 자리가 되어야 한다.
    bigger = N-idx-1
    if idx == 0:
        # 첫번째 놈은 어차피 본인보다 작은놈이 없으니까 바로 위치시키기
        result[n] = idx+1
    else:
        zero = 0
        for i in range(N):
            if n == zero and result[i] == 0:
                result[i] = idx + 1
                break
            if result[i] == 0:
                zero += 1

print(' '.join(map(str, result)))