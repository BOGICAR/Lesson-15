import re
user_input = input()


def match(u_input):
    if bool(re.search(r'[a-z]', u_input)) is False:
        print('Enter аt least 1 symbol from a-z')
    else:
        if bool(re.search('[A-Z]', u_input)) is False:
            print('Enter аt least 1 symbol from A-Z')
        else:
            if bool(re.search('[0-9]', u_input)) is False:
                print('Enter аt least 1 symbol from 0-9')
            else:
                if bool(re.search('[$#@+=-]', u_input)) is False:
                    print('Enter аt least 1 symbol of $#@+=-')
                else:
                    if len(user_input) >= 8:
                        print('Password is correct')
                    else:
                        print('Enter аt least 8 symbols')


match(user_input)
