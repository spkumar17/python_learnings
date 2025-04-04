# Method Overloading and Method Overriding in Python

## Method Overloading

### What is Method Overloading?
Method Overloading allows a class to have multiple methods with the same name but different arguments. However, **Python does not support true method overloading** like Java or C++. Instead, we can achieve similar behavior using default arguments or `*args` and `**kwargs`.

### Example:
```python
class MathOperations:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c  # If three arguments are given
        return a + b  # If two arguments are given

math_op = MathOperations()
print(math_op.add(2, 3))      # Output: 5
print(math_op.add(2, 3, 4))   # Output: 9
```

### Key Points:
- Python allows overloading by **using default parameters** or `*args, **kwargs`.
- Unlike Java, we cannot define multiple methods with the same name but different parameters.

---

## Method Overriding

### What is Method Overriding?
Method Overriding allows a **child class** to provide a **specific implementation** of a method that is already defined in its **parent class**.

### Example:
```python
class Parent:
    def show_message(self):
        return "This is the Parent class"

class Child(Parent):
    def show_message(self):
        return "This is the Child class"  # Overriding the method

obj1 = Parent()
obj2 = Child()

print(obj1.show_message())  # Output: This is the Parent class
print(obj2.show_message())  # Output: This is the Child class
```

### Key Points:
- **Overriding happens in inheritance.**
- The method in the **child class** must have the **same name** as in the **parent class**.
- The child class method replaces the parent class method when called through a child class instance.

---

## Differences Between Method Overloading & Method Overriding

| Feature              | Method Overloading | Method Overriding |
|---------------------|----------------|----------------|
| Definition          | Multiple methods with the same name but different parameters | Redefining a method from the parent class in a child class |
| Supported in Python? | No, but can be achieved using default arguments or `*args` | Yes, using inheritance |
| Occurs in           | Same class      | Parent-child relationship |
| Purpose            | Provides multiple ways to call a method | Allows a subclass to customize behavior |
| Example            | `add(a, b)`, `add(a, b, c)` | Redefining `show_message()` in `Child` class |

---

## Summary
- **Method Overloading** is **not natively supported** in Python but can be achieved using default arguments or `*args`.
- **Method Overriding** is used in **inheritance** to modify the behavior of a method in a child class.
- Overriding allows flexibility, whereas overloading (if simulated) provides multiple ways to call a method.

``` python 

# Method overloading

class MathOperations:
    def add(self, a = None, b = None , c = None):
        s = 0
        
        if a != None and b != None and  c != None:
            return a + b + c  # If three arguments are given
        elif a != None and b != None:
            return a + b
        elif a != None:
            return a
        return s

math_op = MathOperations()
print(math_op.add(2, 3))      # Output: 5
print(math_op.add(2, 3, 4))   # Output: 9

```

``` python
# without the method show_message in child class 

class Parent:
    def show_message(self):
        return "This is the Parent class"

class Child(Parent):
    pass
    
obj1 = Parent()
obj2 = Child()

print(obj1.show_message())  # Output: This is the Parent class
print(obj2.show_message())  # Output: This is the Parent class

```

```python

# with the method show_message in child class 

class Parent:
    def show_message(self):
        return "This is the Parent class"

class Child(Parent):
    def show_message(self):
        return "This is the Child class"  # Overriding the method

obj1 = Parent()
obj2 = Child()

print(obj1.show_message())  # Output: This is the Parent class
print(obj2.show_message())  # Output: This is the Child class

```