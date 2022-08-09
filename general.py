from recursion import extension
from recursion import recursion
import check


def main():
    site = check.is_site_valid()
    depth = check.is_depth_valid()
    links_list = extension(site)
    recursion(links_list, depth)


if __name__ == '__main__':
    main()