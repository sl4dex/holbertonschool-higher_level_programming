#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
        return res
    except BaseException as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
