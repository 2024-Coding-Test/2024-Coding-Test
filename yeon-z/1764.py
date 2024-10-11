N, M = map(int, input().split())

not_hear = set([])
not_see = set([])

for _ in range(N):
    not_hear.add(input().strip())

for _ in range(M):
    not_see.add(input().strip())

not_hear_and_see = list(not_hear.intersection(not_see))
not_hear_and_see.sort()
print(len(not_hear_and_see))
for a in not_hear_and_see:
    print(a)