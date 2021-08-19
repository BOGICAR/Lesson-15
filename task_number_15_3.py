import re
user_input = input()


def match(u_input):
    if not re.search(r'[a-z]', u_input):
        return 'Enter аt least 1 symbol from a-z'
    if not re.search('[A-Z]', u_input):
        return 'Enter аt least 1 symbol from A-Z'
    if not re.search('[0-9]', u_input):
        return 'Enter аt least 1 symbol from 0-9'
    if not re.search('[$#@+=-]', u_input):
        return 'Enter аt least 1 symbol of $#@+=-'
    if len(user_input) < 8:
        return 'Enter аt least 8 symbols'
    return 'Password is correct'


print(match(user_input))
