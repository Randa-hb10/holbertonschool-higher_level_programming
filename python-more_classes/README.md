# 0x08. Python - More Classes and Objects

## Project
Learning **OOP in Python** by creating a `Rectangle` class with attributes, methods, class/static methods, and string representations.

## Files & Tasks

| File | Description |
|------|------------|
| 0-rectangle.py | Empty class. |
| 1-rectangle.py | Width & height with getters/setters. |
| 2-rectangle.py | `area()` & `perimeter()`. |
| 3-rectangle.py | `__str__()` to print rectangle. |
| 4-rectangle.py | `__repr__()` to recreate instance. |
| 5-rectangle.py | `__del__()` prints message. |
| 6-rectangle.py | Class attribute `number_of_instances`. |
| 7-rectangle.py | Class attribute `print_symbol`. |
| 8-rectangle.py | Static method `bigger_or_equal()`. |
| 9-rectangle.py | Class method `square()` to create squares. |

## Features
- Private attributes `__width`, `__height` with validation.  
- Properties for `width` and `height`.  
- `area()` and `perimeter()`.  
- `__str__()` and `__repr__()`.  
- Class attributes: `number_of_instances`, `print_symbol`.  
- Destructor prints `"Bye rectangle..."`.  
- Static method: `bigger_or_equal()`.  
- Class method: `square()`.

## Example

```python
Rectangle = __import__('9-rectangle').Rectangle

sq = Rectangle.square(5)
print(sq.area(), sq.perimeter())
print(sq)


