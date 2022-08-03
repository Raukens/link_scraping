import sys
from test import extension
from check import recursion

url = sys.argv
general_list = [url]


def main():
    links_list = extension(url)
    recursion(links_list)
    for link in general_list:
        print(link)


if __name__ == '__main__':
    main()