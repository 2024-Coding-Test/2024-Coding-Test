from sys import stdin

N = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))
_arr = arr.copy()
_arr.sort()

dict = {}
result = []

for i in range(N):
    if _arr[i] not in dict:
        dict[_arr[i]] = len(dict)

for a in arr:
    result.append(dict[a])

print(" ".join(map(str, result)))