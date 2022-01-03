#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        fWord = None
    else:
        fWord = sentence[0]
    return len(sentence), fWord
