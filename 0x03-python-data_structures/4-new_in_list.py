#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = []
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        for i in my_list:
            new.append(i)
        new[idx] = element
        return new

