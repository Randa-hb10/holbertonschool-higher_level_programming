#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    name = set()
    for item in set_1:
        if item not in set_2:
            name.add(item)
    for item in set_2:
        if item not in set_1:
            name.add(item)
    return name
