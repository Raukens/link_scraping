from check import extension
from check import recursion
from interface import get_user_data


def main():
    input_list = get_user_data()
    site = input_list[0]
    depth = input_list[1]
    general_list = input_list[2]
    links_list = extension(site)
    recursion(general_list, links_list, depth)
    for link in general_list:
        print(link)


if __name__ == '__main__':
    main()