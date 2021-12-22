#!/usr/bin/python3
def uppercase(str):
    # desde 0 hasta el largo del string
    for i in range(len(str)):
        letter = str[i]
        if ord(letter) in range(97, 123):
            letter = chr(ord(letter) - 32)
        print("{}".format(letter), end="")
    print("")
