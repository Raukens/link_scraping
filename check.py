import main

import test


def recursion(links_list, iteration=2):
    space1 = '\t' * 1
    space2 = '\t' * 2
    if iteration > 0:
        for link in links_list:
            main.general_list.append(space1)
            main.general_list.append(link)
            sub_list = test.extension(link)
            main.general_list.append(space2)
            main.general_list.append(sub_list)
        return recursion(links_list, iteration=iteration - 1)
    else:
        return main.general_list



