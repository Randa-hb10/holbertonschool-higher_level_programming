# Holberton School - Python Classes: Square

This project is a series of Python tasks implementing a `Square` class, progressively adding features to understand **Object-Oriented Programming (OOP)** in Python.

---

## Tasks Summary (0-6)

### Task 0: Empty Class
- Created an **empty `Square` class**.
- Learned how to instantiate objects and inspect their type and dictionary.

### Task 1: Private Attribute `__size`
- Added **private instance attribute** `__size`.
- Practiced encapsulation: attributes cannot be accessed directly outside the class.

### Task 2: Validate Size
- Added **validation** in the constructor (`__init__`):
  - `size` must be an integer (`TypeError` if not)
  - `size` must be >= 0 (`ValueError` if not)
- Learned to handle invalid input during instantiation.

### Task 3: Area Method
- Added method `area()` to compute the square's area.
- Practiced defining **public instance methods** that use private attributes.

### Task 4: Getter and Setter for Size
- Introduced **property decorator** (`@property`) and **setter** (`@size.setter`) for `size`.
- Centralized type/value validation in the setter.
- Learned Pythonic OOP encapsulation techniques.

### Task 5: Printing the Square
- Added `my_print()` method:
  - Prints the square using the `#` character.
  - Prints an **empty line** if size is 0.
- Practiced **behavior based on object attributes**.

### Task 6: Position Attribute
- Added **private `__position` attribute** with getter/setter:
  - Must be a tuple of 2 positive integers `(x_offset, y_offset)`.
- Updated `my_print()` to respect `position`:
  - Vertical offset (`position[1]`) → empty lines before the square.
  - Horizontal offset (`position[0]`) → spaces before each `#`.
- Learned **how object state can affect method behavior**.

---

## Skills Learned

- Private attributes, encapsulation, and information hiding  
- Property decorators for getters and setters  
- Type and value validation in Python  
- Writing public methods that interact with object state  
- Pythonic OOP design principles  
- Printing structured data with formatting  

---

