#!/usr/bin/env python3

def islower(c):
    """Check if a character is lowercase."""
    if len(c) == 0:
        return False
    
    ascii_val = ord(c[0])
    
    # Check if ASCII value is between 'a' (97) and 'z' (122)
    if 97 <= ascii_val <= 122:
        return True
    else:
        return False


# Code to allow direct execution
if __name__ == "__main__":
    # Test cases from the example
    print("a is {}".format("lower" if islower("a") else "upper"))
    print("H is {}".format("lower" if islower("H") else "upper"))
    print("A is {}".format("lower" if islower("A") else "upper"))
    print("3 is {}".format("lower" if islower("3") else "upper"))
    print("g is {}".format("lower" if islower("g") else "upper"))
