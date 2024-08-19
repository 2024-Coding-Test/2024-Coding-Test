n,k = map(int,input().split()) # n : 국가 수, k : 등수를 알고 싶은 국가
country = []; medal = [] # 국가와 해당 국가의 메달 개수 리스트
for _ in range(n):
    c,*m = list(map(int,input().split()))
    country.append(c)
    medal.append(m)

# 메달 수 금메달 -> 은메달 -> 동메달 순으로 정렬
sorted_medal = sorted(medal, key = lambda x: (-x[0], -x[1], -x[2]))

# 국가 순위 구하기
# 입력으로 주어진 메달 순서대로 해당 메달이 정렬되었을 때 어디에 위치한지 계산
rank = [sorted_medal.index(c) + 1 for c in medal]

print(rank[country.index(k)])