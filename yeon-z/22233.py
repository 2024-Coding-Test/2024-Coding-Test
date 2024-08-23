# 가희의 키워드
# 총 N개의 메모 존재
# 최대 10개의 키워드에 대해 글 작성
# 메모장에 있던 키워드는 글을 쓴 이휴 지워지게 된다.
# 메모장에 있는 키워드 개수 몇개인지

# 글을 쓴 후 남아있는 메모장 키워드 수 출력
# 키워드 중복 X

from sys import stdin

# N: 메모장에 적은 키워드 수
# M: 블로그 글 쓴 개수
N, M = map(int, stdin.readline().strip().split())

memo = set()

for _ in range(N):
    # 메모장 키워드
    keywords = stdin.readline().strip().split(',')
    for k in keywords:
        memo.add(k)
for _ in range(M):
    # 블로그 글 작성
    keywords = stdin.readline().strip().split(',')
    for k in keywords:
        if k in memo:
            memo.remove(k)
    print(len(memo))