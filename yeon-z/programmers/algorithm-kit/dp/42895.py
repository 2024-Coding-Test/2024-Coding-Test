def solution(N, number):
    if N == number:
        return 1

    # 1부터 8까지의 집합을 저장할 리스트
    s = [set() for x in range(8)]

    for i in range(8):
        s[i].add(int(str(N) * (i + 1)))
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        if number in s[i]:
            return i + 1

    return -1
