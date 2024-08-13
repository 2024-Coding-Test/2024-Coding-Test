consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowel = ['a','e','i','o','u']

while True:
    password = input()
    is_accept = 0

    if password == 'end':
        break

    if all(word not in vowel for word in password):
        print(f'<{password}> is not acceptable.')

    else:
        for i in range(1,len(password)-1):
            if password[i-1] in consonant and password[i] in consonant and password[i+1] in consonant:
                print(f'<{password}> is not acceptable.')
                is_accept = 1
                break
            elif password[i-1] in vowel and password[i] in vowel and password[i+1] in vowel:
                print(f'<{password}> is not acceptable.')
                is_accept = 1
                break
            elif password[i-1] == password[i]:
                if (password[i-1] == 'e' and password[i] == 'e') or (password[i-1] == 'o' and password[i] == 'o'):
                    pass
                else:
                    print(f'<{password}> is not acceptable.')
                    is_accept = 1
                    break
            elif password[i] == password[i+1]:
                if (password[i] == 'e' and password[i+1] == 'e') or (password[i] == 'o' and password[i+1] == 'o'):
                    pass
                else:
                    print(f'<{password}> is not acceptable.')
                    is_accept = 1
                    break
        
        if is_accept == 0:
            print(f'<{password}> is acceptable.')
    