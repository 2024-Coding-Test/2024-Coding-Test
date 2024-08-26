def solution(answers):
    one_list = [1,2,3,4,5]
    two_list = [2,1,2,3,2,4,2,5]
    thr_list = [3,3,1,1,2,2,4,4,5,5]
    scores = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == one_list[idx % len(one_list)]:
            score[0] += 1
        if answer == two_list[idx % len(two_list)]:
            score[1] += 1
        if answer == thr_list[idx % len(thr_list)]:
            score[2] += 1

    for idx, score in enumerate(scores):
        if score == max(scores):
            result.append(idx + 1)

    return result