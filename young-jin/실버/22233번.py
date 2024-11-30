import sys
# sys.stdin.readline()으로 입력을 받게 된다면 속도는 빠르지만 개행문자를 포함하기 때문에 제거해줘야 함
input = sys.stdin.readline() 

n,m = map(int,input().split()) # n : 키워드 개수, m : 글 개수
keywords = set(input().strip() for _ in range(n)) 

for _ in range(m):
    post = set(input().strip().split(','))
    while post:
        p = post.pop()
        keywords.discard(p)
    print(len(keywords))
