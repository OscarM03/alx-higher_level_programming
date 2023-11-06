def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        new_tuple = (length, sentence[0])
        return new_tuple
    else:
        new_tuple = (0, None)
        return new_tuple
