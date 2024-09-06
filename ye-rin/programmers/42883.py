def solution(number, k):
    stack = []
    
    for num in number:
        # k는 제거할 수 있는 자릿수의 개수
        # stack이 비어있지 않고, stack의 top이 현재 num보다 작으며, 제거할 자릿수가 남아있다면,
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
        
    # k가 남아 있는 경우, stack에서 끝에서부터 제거
    return ''.join(stack[:len(stack) - k])