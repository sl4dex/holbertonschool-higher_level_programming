#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        hiscore = 0
        for person, score in a_dictionary.items():
            if score > hiscore:
                hiscore = score
                winner = person
    return winner
