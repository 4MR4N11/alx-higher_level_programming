#!/usr/bin/python3
def best_score(a_dictionary):
    tmp = 0
    if not a_dictionary:
        return None
    else:
        tmp = sorted(a_dictionary.values()).pop()
        for key, value in a_dictionary.items():
            if value == tmp:
                return key
        return None
    return None
