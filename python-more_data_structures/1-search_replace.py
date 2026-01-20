#!/usr/bin/python3
def search_replace(my_list, search, replace):
    value = []
    for number in my_list:
        if number == search:
            value.append(replace)
        else:
            value.append(number)
    return value
