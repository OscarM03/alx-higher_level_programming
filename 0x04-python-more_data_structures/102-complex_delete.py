#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        delete = []
        for c, y in a_dictionary.items():
            if y == value:
                delete.append(c)
        if delete != []:
            length = len(delete)
            j = 0
            while length > 0:
                a_dictionary.pop(delete[j])
                j += 1
                length -= 1
        return a_dictionary
