import re
import csv
user_input = input()


def check_car(u_input):
    if bool(re.fullmatch(r'([А-ЯA-Z]){2}\d{4}[А-ЯA-Z]{2}', u_input)) is True:
        return True
    else:
        return False


def open_csv():
    with open('ua_auto.csv', 'r+', encoding='utf-8') as file:
        reader = csv.reader(file)
        list_ = []
        for i in reader:
            list_.append(i)
        return list_


def check_car_csv(list_, u_input):
    for i in list_:
        if bool(i[1] or i[2] == u_input[:2]) is True:
            return True
        else:
            return False


if check_car(user_input) == check_car_csv(open_csv(), user_input):
    print('The car number is correct')
else:
    print('The car number is not correct')
