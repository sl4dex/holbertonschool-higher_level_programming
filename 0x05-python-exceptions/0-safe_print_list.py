#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    for pos in range(0, x):
        try:
            print(my_list[pos], end="")
        except IndexError:
            break
        else:
            printed += 1
    print()
    return printed
