import re
user_input = input()


def task_15_2(u_input):
    match = re.sub(r'(\d).*(\d).*(\d).*(\d).*(\d).*(\d).*(\d).*(\d).*(\d).*(\d).*',
                   r'(+38) 0\2\3 \4\5\6-\7\8-\9\10', u_input)
    print(match)
    if bool(re.fullmatch(r'\(\+38\)\s0\d{2}\s\d{3}-\d{2}-\d{2}', match)) is True:
        return print('Ok')
    else:
        return print('Failed to recognize number')


task_15_2(user_input)
