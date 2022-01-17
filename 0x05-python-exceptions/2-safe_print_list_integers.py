#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for pos in range(0, x):
        try:
            print("{:d}".format(my_list[pos]), end="")
        except (ValueError, TypeError):
            pass
        else:
            printed += 1
    print()
    return printed
