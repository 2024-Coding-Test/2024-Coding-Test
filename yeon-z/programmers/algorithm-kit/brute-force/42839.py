# 소수 찾기
# 현재 코드
from itertools import permutations


def solution(numbers):
    answer = set([])
    numbers = list(numbers)
    permutation = []

    for n in range(1, len(numbers) + 1):
        nums = [int(''.join(p)) for p in list(permutations(numbers, n))]
        permutation += nums

    permutation = set(permutation)

    for p in list(permutation):
        flag = True
        if p < 2:
            flag = False
        else:
            for i in range(2, p):
                if p % i == 0:
                    flag = False
                    break
        if flag:
            answer.add(p)
    return len(answer)

# 이전 코드
from itertools import permutations


def solution(numbers):
    answer = []
    numbers = list(numbers)
    perm = []

    for i in range(1, len(numbers) + 1):
        perm += list(permutations(numbers, i))

    nums = [int(("".join(p))) for p in perm]
    nums = list(set(nums))

    for n in nums:
        flag = True
        if n < 2:
            flag = False

        for i in range(2, n):
            if n % i == 0:
                flag = False
                break
        if flag:
            answer.append(n)

    return len(answer)


