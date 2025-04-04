# Overloading Operators in Python: The Point Class Example

## Introduction
Operator overloading in Python allows us to redefine the behavior of built-in operators for user-defined classes. This feature enables intuitive operations on custom objects. In this example, we define a `Point` class that supports addition (`+`) and greater-than (`>`). The `__repr__` method is used to provide a meaningful string representation of `Point` instances.

---

## Code Explanation

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x1 = self.x + other.x
        x2 = self.y + other.y
        return x1, x2
        
    def __repr__(self):
        return f"Point({self.x}, {self.y})"  
        
    def __gt__(self, other):
        x1 = self.x + self.y
        x2 = other.x + other.y
        
        if x1 > x2:  # Equivalent to p1.__gt__(p2) ---> p1.x + p1.y > p2.x + p2.y
            return f"{self} is greater"
        elif x1 < x2:  # Equivalent to p1.__gt__(p2) ---> p1.x + p1.y < p2.x + p2.y
            return f"{other} is greater"
        else:
            return f"both {self} and {other} are equal"    
    
p1 = Point(2, 3)
p2 = Point(4, 5)

# Using overloaded comparison operator
result = p1 > p2
print(result)
```

---

## Detailed Explanation

### 1. `__init__` (Constructor)
The `__init__` method initializes a `Point` object with two attributes: `x` and `y`.

### 2. `__add__` (Overloading `+` Operator)
The `__add__` method allows adding two `Point` objects by summing their respective `x` and `y` coordinates and returning the result as a tuple.

### 3. `__repr__` (String Representation of Objects)
The `__repr__` method provides a meaningful representation of `Point` objects. When `repr()` or `print()` is called on an instance, it returns a string in the format `Point(x, y)`.

#### **How `__repr__` Works in This Example:**
- Whenever we use `print(p1)` or `print(p2)`, it returns `Point(2, 3)` and `Point(4, 5)`, respectively.
- Inside `__gt__`, when we use `f"{self}"`, it invokes `__repr__()`, which helps in printing a meaningful message like:
  - `Point(2, 3) is greater`
  - `Point(4, 5) is greater`
  - `both Point(2, 3) and Point(4, 5) are equal`

### 4. `__gt__` (Overloading `>` Operator)
The `__gt__` method compares two `Point` objects by summing their `x` and `y` values and determining which is greater.
- **`self` represents the first operand** (e.g., `p1` when calling `p1 > p2`).
- **`other` represents the second operand** (e.g., `p2` when calling `p1 > p2`).

### 5. Executing the Comparison
When we execute:
```python
result = p1 > p2
```
Python internally calls:
```python
result = p1.__gt__(p2)
```
- If `p1.x + p1.y > p2.x + p2.y`, it returns `"Point(2, 3) is greater"`.
- If `p1.x + p1.y < p2.x + p2.y`, it returns `"Point(4, 5) is greater"`.
- If the sums are equal, it returns `"both Point(2, 3) and Point(4, 5) are equal"`.

---

## Summary
- **Operator overloading** enables customized behavior for built-in operators.
- **`__repr__` is useful for debugging and meaningful output.**
- **The `>` operator is overloaded** to compare the sum of coordinates of two `Point` objects.
- **Python internally calls `p1.__gt__(p2)` when `p1 > p2` is used.**

This implementation provides an intuitive way to compare custom objects in Python.

