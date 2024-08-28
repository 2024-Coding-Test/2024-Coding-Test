# 의상
# 현재 코드
def solution(clothes):
    answer = 1
    clothes_hash = {}
    for name, types in clothes:
        if types not in clothes_hash:
            clothes_hash[types] = [name]
        else:
            clothes_hash[types].append(name)
    print(clothes_hash)

    keys = clothes_hash.keys()
    for key in keys:
        answer *= (len(clothes_hash[key]) + 1)

    return answer - 1

# 이전 코드
def solution(clothes):
    answer = 1
    dict = {}
    for c in clothes:
        if c[1] not in dict:
            dict[c[1]] = [c[0]]
        else:
            dict[c[1]].append(c[0])

    keys = dict.keys()
    for key in keys:
        answer *= (len(dict[key]) + 1)

    return answer -1