def transform(S, T):
    while len(T) > len(S):
        if T[-1] == 'A':
            T = T[:-1]
        elif T[-1] == 'B':
            T = T[:-1][::-1]
    return 1 if T == S else 0

S = input().strip()
T = input().strip()

print(transform(S, T))
