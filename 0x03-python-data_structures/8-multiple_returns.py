#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tup_ret = len(sentence), None
        return tup_ret
    tup_ret = len(sentence), sentence[0]
    return tup_ret
