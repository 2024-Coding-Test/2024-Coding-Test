# 문자열 교환
# a와 b로만 이루어진 문자열이 주어질 때, a를 모두 연속으로 만들기 위해서 필요한 교환의 횟수를 최소로 하는 프로그램
# 문자열 원형임, 처음과 끝은 서로 인접해 있음.
# ex) aabbaaabaaba가 주어졌을 때 2번의 교환이면 a를 모두 연속으로 만들 수 있음.

from sys import stdin

n = list(stdin.readline().strip())
aCount = n.count('a')

n = n + n
minCount = 1001

for i in range(len(n)//2):
    temp = n[i: i + aCount]
    minCount = min(minCount, temp.count('b'))

print(minCount)