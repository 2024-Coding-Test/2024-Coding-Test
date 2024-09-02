def solution(phone_book):
    n = len(phone_book)
    for i in range(n):
        for j in range(n):
            if i != j:
                if phone_book[j].startswith(phone_book[i]):
                    return False
    return True
