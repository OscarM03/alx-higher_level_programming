#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list1 = my_list.copy()
    
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        new_list1[idx] = element
        return new_list1