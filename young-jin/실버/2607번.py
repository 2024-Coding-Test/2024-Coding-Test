n = int(input())
words = [list(input()) for i in range(n)]
answer = 0

first = words[0] # 기준 단어

for i in range(1,n):
    l = len(words[i]) # 문자의 개수
    for w in first:
        if w in words[i]:
            words[i].remove(w) # 기준 단어와 문자가 겹치면 삭제
    if len(words[i]) == 0: # 문자가 다 겹칠 때
        # 문자 하나 더하거나 빼면 기준 단어와 같아 지는 경우 또는 기준 단어와 같은 단어인 경우 비슷한 단어임
        if (abs(len(first)-l) == 1) or (abs(len(first)-l) == 0):
            answer += 1
    elif len(words[i]) == 1: # 문자 하나 빼고 다 겹칠 때
        if l == 1 and words[i][0] not in first: # 단어에 문자가 하나 뿐이고 그 문자가 기준 단어에 없는 경우는 비슷한 단어가 아님
            pass
        elif l < len(first): # 기준 단어보다 문자 수가 적은데 안 겹치는 문자가 하나 뿐이면 비슷한 단어가 아님
            pass
        else: # 그 외의 경우는 다 비슷한 단어
            answer += 1

print(answer)
