#!/usr/bin/python3
pos = 91
while pos > 65:
    if pos % 2 == 0:
        pos -= 33
    else:
        pos += 31
    print("{}".format(chr(pos)), end="")
