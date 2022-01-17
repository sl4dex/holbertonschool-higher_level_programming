#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        # or sys.stderr.write("Exception: " + err + \n")
        print("Exception: " + str(err), file=sys.stderr)
        return False
