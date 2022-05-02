#!/usr/bin/python3
def multiple_returns(sentence):
    lsen = list(sentence)
    tuple_a = (len(lsen), lsen[0])
    if len(lsen) == 0:
        lsen[0] = None
    return tuple_a
