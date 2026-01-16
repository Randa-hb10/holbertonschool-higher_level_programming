#!/usr/bin/python3

def print_last_digit(number):
    """Prints and returns the last digit of a number."""
    
    # Get the absolute value to handle negative numbers
    abs_number = number if number >= 0 else -number
    last_digit = abs_number % 10
    print(last_digit, end='')
    return last_digit
