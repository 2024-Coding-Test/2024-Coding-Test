def is_acceptable(password):
    vowels = set('aeiou')
    accept_exceptions = {'ee', 'oo'}

    # 모음(a,e,i,o,u) 하나를 반드시 포함하는지 확인
    if not any(char in vowels for char in password):
        return False

    # 모음이 3개 혹은 자음이 3개 연속인지 확인
    for i in range(len(password) - 2):
        if (password[i] in vowels and password[i + 1] in vowels and password[i + 2] in vowels) or \
           (password[i] not in vowels and password[i + 1] not in vowels and password[i + 2] not in vowels):
            return False

    # 같은 글자가 연속적으로 두번 오는지 확인 (ee 와 oo는 허용)
    for i in range(len(password) - 1):
        if password[i] == password[i + 1] and password[i:i + 2] not in accept_exceptions:
            return False

    return True


while True:
    password = input()
    if password == 'end':
        break

    if is_acceptable(password):
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')
