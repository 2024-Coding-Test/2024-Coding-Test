# 전화번호 목록
# 현재 코드
def solution(phone_book):
    phone_book.sort()
    prev = phone_book[0]

    for i in range(1, len(phone_book)):
        if prev == phone_book[i][:len(prev)]:
            return False
        prev = phone_book[i]
    return True

# 이전 코드
def solution(phone_book):
    phone_book.sort()
    prev = phone_book[0]
    for i in range(1, len(phone_book)):
        n = len(prev)
        if phone_book[i][:n] == prev:
            return False
        prev = phone_book[i]
    return True