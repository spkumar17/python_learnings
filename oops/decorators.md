# Understanding Python Decorators - Example and Breakdown
A decorator in Python is a function that takes another function as input, adds some additional behavior to it before or after it runs, and returns a new function with the added behavior — without modifying the original function's code.

## Example Code

```python
# Define the decorator function
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called")
        result = func(*args, **kwargs)  # Calls the original function
        print("After the function is called")
        return result
    return wrapper  # Returns the modified function

# Apply the decorator to the add function
@my_decorator
def add(a, b):
    return a + b

# Calling the decorated function
print(add(3, 5))  # Calls wrapper(3, 5) instead of add(3, 5)
```

## Breakdown of Execution Flow

1. **Decorator is applied** → `@my_decorator` means `add = my_decorator(add)`.
2. **Now ****`add`**** is replaced with ****`wrapper`**, so calling `add(3,5)` is actually calling `wrapper(3,5)`.
3. **Inside ****`wrapper(3, 5)`****:**
   - `print("Before the function is called")` is executed.
   - `func(*args, **kwargs)` is called, where `func` is the original `add` function.
   - `add(3, 5)` executes and returns `8`.
   - `result = 8` is stored.
   - `print("After the function is called")` is executed.
   - `wrapper` returns `8`.
4. **Final Output** → `print(add(3, 5))` prints `8`.

### Decorator (my_decorator):

* my_decorator is the outer function that takes the original function (add) and returns the wrapper.

* It is the "decorator" because it decorates the original add function with additional behavior.

### Wrapper (wrapper):

* The wrapper function is inside the decorator.

* It adds extra behavior (e.g., printing before and after the function) and then calls the original add function.

* It returns the result of calling add (or any function being decorated).

### Key Takeaway

Calling `add(3, 5)` **does NOT call ****`my_decorator(add)`**** again**—that happened once when Python processed `@my_decorator`. Instead, it calls `wrapper(3, 5)`, which executes the original `add` function inside it (`func(*args, **kwargs)`). 🚀


## Wrapper
```
wrapper:
 ┌─────────────────────────────┐
 │ print("Before")             │
 │ ┌───────────────────────┐   │
 │ │   original function   │   │  ← This is `func()`
 │ └───────────────────────┘   │
 │ print("After")              │
 └─────────────────────────────┘
```

## 🧠 Is my_decorator a "main function" or a "supporting function"?
my_decorator is not the main function; it's a supporting function that enhances the behavior of another function (in this case, the add function).

Here’s why:

**Main function:** The function that you are actually calling to perform an operation or action. In this case, the add(a, b) function is the "main" function. It performs the core task of adding two numbers.

**Supporting function:** A function (like my_decorator) that modifies or enhances the behavior of the main function without changing its core logic.


## 🧠 Relationship between Wrapper and Decorator:
**The Decorator:**

* It is the outer function that takes the original function as an argument and returns a modified function (often called the wrapper).

* The decorator is responsible for applying additional functionality (like logging, validation, etc.) around the original function.

**The Wrapper:**

* The wrapper is the inner function inside the decorator that wraps the original function.

* It contains the extra behavior (e.g., logging, validation) and calls the original function in the middle.

* The wrapper takes the same arguments as the original function and returns the result after calling the original function.


### 🚀 Can They Be Seen Separately?
Yes, you can view them separately, but they are interlinked in the sense that:

* The decorator (my_decorator) returns the wrapper.

* The wrapper contains the behavior that modifies the original function.

However, if you separate them, you would not have the full functionality of a decorator, since the wrapper is what actually runs when the decorated function is called.


## 🧠 Your Understanding:

* **Function You Want to Extend:** You have a function, and you want to extend its capabilities (e.g., adding logging, validation, or any additional behavior) without modifying its original code.

* **Decorator:** The decorator is a supporting function that allows you to add extra behavior around the function. It wraps the function to enhance its capabilities. The decorator is not modifying the function itself, but it allows you to inject extra functionality before or after the function runs.

* **Wrapper:** The wrapper function is defined inside the decorator. It contains the extra functionality (like logging, timing, etc.) and calls the original function (the one being decorated). The wrapper function is responsible for executing the original function while also adding the new behavior.

