n, new, p = map(int,input().split())
if n:
    score = list(map(int,input().split()))
else:
    score = []

if len(score) >= p and score[-1] >= new:
    print(-1)

elif len(score) == 0:
    print(1)

else:
    if score[n//2] >= new:
        for i in range(n//2, n):
            if min(score) > new:
                score.append(new)
            if score[i] <= new:
                score.insert(i, new)
                break
    else:
        for i in range(n//2, -1, -1):
            if max(score) < new:
                score.insert(0, new)
            if score[i] >= new:
                score.insert(i+1, new)
                break

    rank = score.index(new)+1
    print(rank)