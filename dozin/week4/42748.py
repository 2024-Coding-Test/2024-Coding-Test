def solution(array, commands):
    ans = []
    for i in commands:
        tmp = array[i[0] - 1:i[1]]
        tmp = sorted(tmp)
        ans.append(tmp[i[2] - 1])
    return ans