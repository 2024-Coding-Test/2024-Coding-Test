import math
from collections import deque
operations = deque([])

while True:
    a = input()
    if a == '=':
        break
    if a in ['/', '+', '-', '*']:
        operations.append(a)
    else:
        operations.append(int(a))
result = operations.popleft()
while operations:
    op = operations.popleft()
    if op in ['/', '+', '-', '*']:
        b = operations.popleft()
        if op == '+':
            result += b
        elif op == '/':
            result = math.floor(result / b)
        elif op == '*':
            result *= b
        else:
            result -= b
print(result)