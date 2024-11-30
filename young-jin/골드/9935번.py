import sys
from collections import deque
input = sys.stdin.readline

moonja = input().strip()
pokbal = input().strip()
l = len(pokbal)
stack = []

for i in range(len(moonja)):
    stack.append(moonja[i])
    if ''.join(stack[-l:]) == pokbal:
        for _ in range(l):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')