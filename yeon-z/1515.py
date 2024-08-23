# 수이어쓰기
# 1부터 N까지 모든 수를 차례대로 공백 없이 한 줄에 다 씀.
# 다솜이가 마음에 드는 숫자 몇개를 지움
# 세준이 N을 되돌리려 함.
# 남은 수를 이어붙인 수가 주어짐
# N의 최솟값을 구해라 > 아무것도 지우지 않을 수도 있음.

# 입력값
# 첫째 줄에 지우고 남은 수를 한 줄로 이어 붙인 수가 주어진다. 이 수는 최대 3,000자리다.

# 출력
# 가능한 N 중에 최솟값을 출력한다.

from sys import stdin
# 다시풀기

N = stdin.readline().strip()

n = 0
while len(N):
    n += 1
    num = str(n)
    while len(num) and len(N):
        if num[0] == N[0]:
            N = N[1:]
        num = num[1:]
print(n)