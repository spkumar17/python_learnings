# __str__ and __repr__ methods

This project demonstrates the difference between the `__str__` and `__repr__` methods in Python by implementing them in a `Person` class.

## Description

In Python, `__str__` and `__repr__` are special methods used to define how objects are represented as strings:
- `__str__`: Provides a user-friendly string representation of an object. It is used when calling `print()` or `str()`.
- `__repr__`: Provides an unambiguous representation, mainly used for debugging.

## Code Example

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """ Returns a user-friendly string representation of the object. """
        return f"{self.name} is {self.age} years old."

    def __repr__(self):
        """ Returns an unambiguous string representation useful for debugging. """
        return f"Person(name='{self.name}', age={self.age})"


# Creating an instance of Person
p = Person("Alice", 30)

# Printing the instsance
print(str(p))   # Calls __str__ -> User-friendly output
print(repr(p))  # Calls __repr__ -> Debugging output

# If you type the object name in interactive mode or inside a list, __repr__ is used
print(p)  # Calls __repr__
```

## Expected Output

```
Alice is 30 years old.
Person(name='Alice', age=30)
Person(name='Alice', age=30)
```

## Key Takeaways
- Use `__str__` for a human-readable representation.
- Use `__repr__` for a developer-friendly, debugging representation.

This example helps to understand when Python internally calls `__str__` and `__repr__` for object representations.

