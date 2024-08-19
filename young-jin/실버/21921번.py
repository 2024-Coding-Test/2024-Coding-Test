import sys
input = sys.stdin.readline

n,x = map(int,input().split())
visitor = list(map(int,input().split()))

window = sum(visitor[:x])
blog_visitor = [window]
max_visitor = window
for i in range(x, n):
    window += visitor[i] - visitor[i-x]
    blog_visitor.append(window)
    max_visitor = max(max_visitor, window)

length = {}
for v in blog_visitor:
    if v not in length:
        length[v] = 1
    else:
        length[v] += 1

if max_visitor == 0:
    print('SAD')
else:
    print(max_visitor)
    print(length[max_visitor])