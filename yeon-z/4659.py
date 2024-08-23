# 비밀번호 발음하기
# 모음(a, e, i, o, u) 하나를 반드시 포함
# 모음 3개 혹은 자음이 3개 연속으로 오면 안된다.
# 같은 글자가 연속적으로 두번 오면 안되나 ee와 oo는 허용한다.

from sys import stdin
mo = ['a', 'e', 'i', 'o', 'u']

while True:
    password = stdin.readline().strip()
    if password == 'end':
        break

    # 모음을 하나라도 포함하고 있는가.
    moin = False
    for m in mo:
        if m in password:
            moin = True
            break


    if moin:
        # 3글자 미만인 경우
        if len(password) == 2:
            # 같은 글자 두개 연속인지만 확인
            prev = ''
            flag = True
            for p in password:
                if prev == p and p != 'e' and p != 'o':
                    flag = False
            if flag:
                print(f'<{password}> is acceptable.')
            else:
                print(f'<{password}> is not acceptable.')
        elif len(password) == 1:
            print(f'<{password}> is acceptable.')

        else:
            # 3글자 이상인 경우
            # 모음이나 자음이 3글자 이상 연속으로 오는지 확인
            isMo = True
            cnt = 0
            flag = False

            for p in password:
                if p in mo:
                    # 모음
                    if isMo == True:
                        cnt += 1
                    else:
                        isMo = True
                        cnt = 1
                else:
                    # 자음
                    if isMo == True:
                        isMo = False
                        cnt = 1
                    else:
                        cnt += 1

                if cnt >= 3:
                    flag = True
                    break

            if flag:
                print(f'<{password}> is not acceptable.')
            else:
                # 같은 글자 두번 이상 확인
                prev = ''
                for p in password:
                    if prev == p and p != 'e' and p != 'o':
                        flag = True
                        break
                    prev = p
                if flag:
                    print(f'<{password}> is not acceptable.')
                else:
                    print(f'<{password}> is acceptable.')
    else:
        # 모음 없음
        print(f'<{password}> is not acceptable.')

