import requests
import interface


def is_site_valid(site=interface.site):

    if '.' in site:
        if 'https://' in site:
            site = str(site)
        else:
            site = str(f"https://{site}")
            response = requests.get(site)
            if response.status_code == 200:
                print('Сайт проходит процедуру парсинга')
    else:
        print('Вы ввели некорректное название сайта. Пожалуйста, попробуйте снова ')
    return site


def is_depth_valid(depth = interface.depth):

    if depth.isdigit():
        depth = int(depth)
    else:
        print('Вы ввели не целое число. Пожалуйста, попробуйте снова ')
    return depth
