import requests

import sys


def get_user_data():

    while True:
        site = sys.argv[1]
        if '.' in site:
            if 'https://' in site:
                site = str(site)
            else:
                site = str(f"https://{site}")
                response = requests.get(site)
                if response.status_code == 200:
                    print('Сайт проходит процедуру парсинга')
        else:
            site = input('Вы ввели некорректное название сайта. Пожалуйста, попробуйте снова ')
        depth = sys.argv[2]
        if depth.isdigit() is True:
            depth = int(depth)
        else:
            depth = input('Вы ввели не целое число. Пожалуйста, попробуйте снова ')

        return [site, depth]


