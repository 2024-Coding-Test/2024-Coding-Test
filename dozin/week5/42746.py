from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1

def solution(numbers):
    # 숫자 배열을 문자열 배열로 변환
    numbers = list(map(str, numbers))
    
    # 커스텀 비교 함수로 정렬
    numbers.sort(key=cmp_to_key(compare))
    
    # 정렬된 문자열들을 이어붙임
    answer = ''.join(numbers)
    
    # 만약 결과가 '0000...' 같은 경우, 0을 반환
    if answer[0] == '0':
        return '0'
    
    return answer
