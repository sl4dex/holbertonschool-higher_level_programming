#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for pos in range(0, x):
            print(my_list[pos], end="")
        return pos + 1
    except IndexError:
        return pos
    finally:
        print()
