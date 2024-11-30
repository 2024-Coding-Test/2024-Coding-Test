from itertools import combinations

L,C = map(int,input().split())
alp = list(input().split())

vowel = [a for a in alp if a in set(['a','e','i','o','u'])]
ans = []

for l in list(combinations(alp, L)):
    n_vowel = 0; n_consonant = 0
    l = sorted(l)
    for a in l:
        if a in vowel:
            n_vowel += 1
        else:
            n_consonant += 1
    
    if n_vowel >= 1 and n_consonant >= 2:
        ans.append(l)

ans.sort()
for a in ans:
    print(''.join(a))