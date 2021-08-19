import re
user_input = input()


def task_15_2(u_input):
    match = re.sub(r'.*(\d{3}).*(\d{3}).*(\d{2}).*(\d{2}).*',
                   r'(+38) \1 \2-\3-\4', u_input)
    if len(match) > 9:
        return match
    else:
        return 'Failed to recognize number'


print(task_15_2(user_input))
