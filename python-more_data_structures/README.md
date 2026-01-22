# Python - More Data Structures: Set, Dictionary

This project focuses on practicing **Python sets and dictionaries** through small functions. The goal is to understand how these data structures work internally and how to manipulate them efficiently **without importing modules**.

---

## Learning Objectives

By completing these tasks, you should be able to:

* Understand and use **sets** and **dictionaries**
* Iterate over dictionaries (keys / values / items)
* Use set operations (intersection, difference)
* Create and return new data structures without modifying originals
* Write clean and readable Python functions

---

## Tasks

### 0. Common elements

**File:** `0-common_elements.py`

Write a function that returns a set of common elements between two sets.

**Prototype:**

```python
def common_elements(set_1, set_2):
```

---

### 1. Only difference of elements

**File:** `4-only_diff_elements.py`

Write a function that returns a set of all elements present in only one set.

**Prototype:**

```python
def only_diff_elements(set_1, set_2):
```

---

### 2. Number of keys

**File:** `5-number_keys.py`

Write a function that returns the number of keys in a dictionary.

**Prototype:**

```python
def number_keys(a_dictionary):
```

---

### 3. Print sorted dictionary

**File:** `6-print_sorted_dictionary.py`

Write a function that prints a dictionary by ordered keys.

* Keys must be sorted alphabetically
* Only first-level keys are sorted

**Prototype:**

```python
def print_sorted_dictionary(a_dictionary):
```

---

### 4. Update dictionary

**File:** `7-update_dictionary.py`

Write a function that replaces or adds a key/value in a dictionary.

* If key exists → replace value
* If key does not exist → create it

**Prototype:**

```python
def update_dictionary(a_dictionary, key, value):
```

---

### 5. Simple delete by key

**File:** `8-simple_delete.py`

Write a function that deletes a key in a dictionary.

* If the key does not exist, the dictionary remains unchanged

**Prototype:**

```python
def simple_delete(a_dictionary, key=""):
```

---

### 6. Multiply values by 2

**File:** `9-multiply_by_2.py`

Write a function that returns a new dictionary with all values multiplied by 2.

* Values are integers
* Original dictionary must not be modified

**Prototype:**

```python
def multiply_by_2(a_dictionary):
```

---

### 7. Best score

**File:** `10-best_score.py`

Write a function that returns the key with the biggest integer value.

* If dictionary is empty or None → return None
* All values are integers

**Prototype:**

```python
def best_score(a_dictionary):
```

---

### 8. Multiply list using map

**File:** `11-multiply_list_map.py`

Write a function that returns a new list with all values multiplied by a number **without using loops**.

* Must use `map`
* File must be maximum 3 lines

**Prototype:**

```python
def multiply_list_map(my_list=[], number=0):
```

---

### 9. Roman to Integer (Technical Interview)

**File:** `12-roman_to_int.py`

Write a function that converts a Roman numeral to an integer.

* Values between 1 and 3999
* If input is not a string or is None → return 0

**Prototype:**

```python
def roman_to_int(roman_string):
```

---

## Requirements

* Python 3
* No module imports allowed
* All files must be executable
* Code must follow PEP8 style

---

Holberton School – Higher Level Programming


