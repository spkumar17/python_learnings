# Abstract Classes in Python

## ✅ What is an Abstract Class?
An abstract class in Python is like a blueprint for its subclasses. It is defined using the `ABC` (Abstract Base Class) module from Python's `abc` library.

### Key Points:
- Acts like a **blueprint** for its subclasses.
- Can have **abstract methods** (methods with no body) that **must** be implemented in any subclass.
- Can also include **regular methods** (fully defined) that can be reused by subclasses.
- **Cannot be instantiated directly**.

---

## 📌 Core Principle
> "An abstract class defines methods that must be implemented in any subclass that inherits from it."

---

## ✅ Example: Abstract Class in Action

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):  # This must be implemented in any subclass
        pass
```

### ❌ This Will Fail:
```python
class Dog(Animal):
    pass

# Attempting to create an object of Dog will raise an error:
d = Dog()
```

### ❗ Error:
```
TypeError: Can't instantiate abstract class Dog with abstract methods make_sound
```

### ✅ Correct Way:
```python
class Dog(Animal):
    def make_sound(self):
        return "Bark"

# Now this works
print(Dog().make_sound())  # Output: Bark
```

---

## 💡 Summary
- Abstract classes enforce a contract.
- They ensure all derived classes implement required behaviors.
- Great for designing frameworks and enforcing consistency across related objects.



# 🧱 Abstract Class Example in Python

```python
from abc import ABC, abstractmethod

class livingbeing(ABC):  # ✅ Abstract Base Class
    @abstractmethod
    def breath(self):
        pass

    @abstractmethod
    def sence(self):
        pass

    def normalmethod(self):
        return "An abstract class can also contains nrml method"


class human(livingbeing):  # ❌ Doesn't implement required abstract methods
    def walk(self):
        return "Able to walk"


class animal(livingbeing):  # ✅ Implements all required abstract methods
    def run(self):
        return "Able to run"

    def breath(self):
        return "Breathing"

    def sence(self):
        return "able to sence the things"


class bird():  # ✅ Independent regular class
    def fly(self):
        return "able to fly"

        

cat = animal()
print(cat.run())
# men = human()
# print(men.walk()) # TypeError: Can't instantiate abstract class human without an implementation for abstract methods 'breath', 'sence'

crow = bird()
print(crow.fly())

```

---

## 📋 Class Analysis Table

| Class Name | Inherits from `livingbeing` | Implements `breath()` | Implements `sence()` | Has Own Method | Instantiable? | Notes |
|------------|-----------------------------|------------------------|-----------------------|----------------|----------------|-------|
| `livingbeing` | —                           | Abstract Method         | Abstract Method        | `normalmethod()` | ❌ No           | Abstract base class |
| `human`       | ✅ Yes                      | ❌ No                   | ❌ No                  | `walk()`        | ❌ No           | Missing abstract methods |
| `animal`      | ✅ Yes                      | ✅ Yes                  | ✅ Yes                 | `run()`         | ✅ Yes          | Valid concrete subclass |
| `bird`        | ❌ No                       | N/A                    | N/A                   | `fly()`         | ✅ Yes          | Regular class |

---

## 🔑 Key Points

- ✅ **Abstract classes** define **what methods must exist** in child classes.
- ❌ **Cannot create objects** of abstract classes or subclasses missing required methods.
- ✅ Abstract class can contain **normal methods**.
- ✅ You can mix abstract and non-abstract classes freely.


