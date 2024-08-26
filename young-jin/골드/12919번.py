# s에서 t로 바꾸는 경우의 수는 많기 때문에, 역으로 t에서 s로 바꿈

import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

def change_word(t):
    if t == s:
        print(1)
        sys.exit()
    elif len(t) == 0:
        return
    else:
        if t[-1] == 'A':
            change_word(t[:-1])
        if t[0] == 'B':
            change_word(t[1:][::-1])

change_word(t)
print(0)