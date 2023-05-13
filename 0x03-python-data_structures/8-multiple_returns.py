#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = ()
    if not sentence:
        new_tuple = (0, None)
        return new_tuple
    new_tuple = (len(sentence), sentence[0])
    return new_tuple
