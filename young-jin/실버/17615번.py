# 처음과 끝 공이 다를 경우 -> 다른 공이 나올 때까지 양 쪽 공 삭제
# 처음과 끝 공이 같을 경우 -> 많은 공이 있는 부분 삭제
# 삭제가 끝난 후 공 개수 최솟값 구하기

import sys
input = sys.stdin.readline

n = int(input())
ball = input().strip()

if len(set(ball)) == 1:
    print(0)

elif ball[0] == ball[n-1]:
    
    color = ball[0]
    count_a = 0
    idx_a = 0
    for i in range(n):
        if ball[i] == color:
            count_a += 1
        else:
            idx_a = i-1
            break

    count_b = 0
    idx_b = 0
    for i in range(n-1,-1,-1):
        if ball[i] == color:
            count_b += 1
        else:
            idx_b = i+1
            break

    if count_a >= count_b:
        ball = ball[idx_a+1:]
    else:
        ball = ball[:idx_b]

else:
    idx_a = 0; idx_b = 0
    for i in range(n):
        if ball[0] == ball[i]:
            pass
        else:
            idx_a = i
            break
    for i in range(n-1,-1,-1):
        if ball[n-1] == ball[i]:
            pass
        else:
            idx_b = i+1
            break

    ball = ball[idx_a:idx_b]

if len(set(ball)) != 1:
    if len(ball) == 0:
        print(0)
    else:
        count = {}
        for c in ball:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1

        print(min(count.values()))