# 올바른 괄호
# 현재 코드
def solution(s):
    answer = False
    # 첫 시작이 ) 이면 False임
    if s[0] == ')':
        return answer

    stack = []
    for _s in s:
        if len(stack) > 0 and stack[-1] == '(' and _s == ')':
            stack.pop()
        else:
            stack.append(_s)

    if len(stack) == 0:
        answer = True

    return answer

# 이전 코드
def solution(s):
    stack = []
    s = list(s)

    def isEmpty(stack):
        return len(stack) == 0

    for i in s:
        if i == ')':
            if isEmpty(stack):
                return False
            if stack[-1] == '(':
                stack.pop()
        else:
            stack.append(i)

    return True if isEmpty(stack) else False
