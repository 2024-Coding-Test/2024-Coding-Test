# 등수 구하기

from sys import stdin
N, score, P = map(int, stdin.readline().strip().split())

if N == 0:
    print(1)
    exit()
rank = list(map(int, stdin.readline().strip().split()))
rank_min = min(rank)

if len(rank) == P and rank_min >= score:
    # rank 자리 꽉찬 상태일 때
    # 태수 점수가 랭커 최저점보다 낮거나 같을때
    print(-1)
else:
    rank.append(score)
    rank.sort(key=lambda x: -x)
    rankList = []
    ranking = 1
    for i in range(len(rank)):
        if i == 0:
            rankList.append(ranking)
        else:
            if rank[i-1] == rank[i]:
                rankList.append(ranking)
            else:
                ranking = len(rankList) + 1
                rankList.append(ranking)
    idx = rank.index(score)
    print(rankList[idx])
