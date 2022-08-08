from recursion import extension
from recursion import recursion
from interface import get_user_data


def main():
    input_list = get_user_data()
    site = input_list[0]
    depth = input_list[1]
    links_list = extension(site)
    recursion(links_list, depth)


if __name__ == '__main__':
    main()