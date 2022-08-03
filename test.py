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