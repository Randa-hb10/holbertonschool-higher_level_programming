#!/usr/bin/python3
def uniq_add(my_list=[]):
    value = []
    total = 0
    for num in my_list:
        if num not in value:
            value.append(num)
            total += num
    return total
