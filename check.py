import requests

from bs4 import BeautifulSoup


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


def recursion(general_list, links_list, iteration):
    space1 = '\t'
    space2 = '\t' * 2
    if iteration > 0:
        for link in links_list:
            general_list.append(space1)
            general_list.append(link)
            sub_list = extension(link)
            general_list.append(space2)
            general_list.append(sub_list)
        return recursion(general_list, links_list, iteration=iteration - 1)
    else:
        return general_list



