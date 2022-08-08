import requests

from bs4 import BeautifulSoup

import sys


def extension(url):

    links_list = []
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for tags in soup.findAll("a"):
        href = tags['href']
        if href.startswith('/') and not href.startswith('//'):
            href = url + href
        if href.startswith(url):
            links_list.append(href)
    links_list = list(set(links_list))
    return links_list


def recursion(links_list, iteration):
    x = int(sys.argv[2]) - iteration
    space = '\t' * (x - iteration)
    if iteration > 0:
        for link in links_list:
            sub_list = extension(link)
            print(f"{space}{link}")
            print(f"{space}{sub_list}")
        return recursion(links_list, iteration=iteration - 1)
    else:
        return links_list



