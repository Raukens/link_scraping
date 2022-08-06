import requests


def get_user_data():

    while True:
        site = input('Введите название сайта ')
        if '.' in site:
            if 'https://' in site:
                site = str(site)
            else:
                site = str(f"https://{site}")
        else:
            print('Вы ввели некорректное название сайта. Пожалуйста, попробуйте снова ')
        response = requests.get(site)
        if response.status_code == 200:
            print('Сайт проходит процедуру парсинга')
        else:
            print('Ошибка соединения с сайтом, возможно вы ввели неправильный адрес сайта')
        depth = input('Введите глубину парсинга: ')
        if depth.isdigit() is True:
            depth = int(depth)
        else:
            print('Вы ввели не целое число. Пожалуйста, попробуйте снова ')
        general_list = [site]

        return [site, depth, general_list]


