#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} argments.".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{} arugment:".format(len(sys.argv) - 1))
        print("{}: {}".format(len(sys.argv) - 1, sys.argv[1]))
    else:
        print("{} arugments:".format(len(sys.argv) - 1))
        for pos in range(len(sys.argv) - 1):
            print("{}: {}".format(pos + 1, sys.argv[pos + 1]))
