import requests


def get_user_data():

    while True:
        site = input('Введите название сайта ')
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
        depth = input('Введите глубину парсинга: ')
        if depth.isdigit() is True:
            depth = int(depth)
        else:
            depth = input('Вы ввели не целое число. Пожалуйста, попробуйте снова ')
        general_list = [site]

        return [site, depth, general_list]


