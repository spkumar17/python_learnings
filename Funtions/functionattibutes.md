
# Function Attributes in Python

## Overview
Python functions have built-in attributes that store metadata about the function. These attributes provide information such as the function name, documentation, module, type hints (annotations), and default argument values.

## Function Attributes
| Attribute | Description |
|-----------|-------------|
| `__name__` | Returns the name of the function |
| `__doc__` | Retrieves the function’s docstring (documentation) |
| `__module__` | Returns the module where the function is defined |
| `__annotations__` | Stores type hints (annotations) of parameters and return type |
| `__defaults__` | Returns default values of arguments |

## Example Usage

```python
import functools

def log_function_metadata(func):
    @functools.wraps(func)  # Preserve function metadata
    def wrapper(*args, **kwargs):
        print(f"Function Name: {func.__name__}")
        print(f"Docstring: {func.__doc__}")
        print(f"Defined in Module: {func.__module__}")
        print(f"Annotations: {func.__annotations__}")
        print(f"Default Arguments: {func.__defaults__}")
        return func(*args, **kwargs)
    return wrapper

@log_function_metadata
def greet(name: str = "Guest", age: int = 25) -> str:
    """Greets a person with their name and age."""
    return f"Hello, {name}! You are {age} years old."

# Calling the function
greet("Alice", 30)
```

## Expected Output
```
Function Name: greet
Docstring: Greets a person with their name and age.
Defined in Module: __main__
Annotations: {'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}
Default Arguments: ('Guest', 25)
```

## Why Use These Attributes?
- Helps in debugging and introspection.
- Useful for decorators to retain function metadata.
- Helps document and enforce function signatures with annotations.
