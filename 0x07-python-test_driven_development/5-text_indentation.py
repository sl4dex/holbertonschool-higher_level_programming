#!/usr/bin/python3
""" text indenter module """


def text_indentation(text):
    """ prints formatted text """
    if type(text) is not str:
        raise TypeError("text must be a string")
    start = 1
    for letter in text:
        if start == 1 and letter == " ":
            continue
        else:
            start = 0
        # if letter == "\"":
        #    continue
        if letter in [".", "?", ":"]:
            print(letter, end="")
            start = 1
            print("\n")
            continue
        print(letter, end="")
