# Duck Typing in Python(Polymorphism)

## Overview
This example demonstrates the concept of **Duck Typing** in Python. The `sub` class does not explicitly require a `cal` instance but works with any object that has an `add()` method and attributes `A` and `B`.

## Code Example
```python
class cal:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def add(self):
        return self.A + self.B

class sub:
    def __init__(self, C):
        self.C = C

    def add1(self, obj):
        print(obj.add())  # Calls add() from obj
        return obj.A + obj.B + self.C  
        
# Create an instance of `cal`
f1 = cal(2, 3)

# Create an instance of `sub`
c1 = sub(5)

# Call add1 method
result = c1.add1(f1)

print(result)  # Output: 10 (2 + 3 + 5)
```

## How Duck Typing Works
- `sub` does not store an instance of `cal`.
- Instead, `add1()` works with **any object** that has:
  - an `add()` method
  - attributes `A` and `B`.
- This allows `sub` to work with different objects without strict type enforcement.

## Difference Between Duck Typing and Composition
| Feature | Duck Typing | Composition |
|---------|------------|-------------|
| Object Storage | Does not store `cal`, just uses it temporarily | Stores an instance of `cal` inside `sub` |
| Flexibility | Works with any object that has `A`, `B`, and `add()` | Only works with a specific instance of `cal` |
| Relationship | Loosely coupled | Tightly coupled |

## Duck Typing in Action
Here’s an example where `FakeCal` is not related to `cal`, but still works:
```python
class FakeCal:
    def __init__(self):
        self.A = 10
        self.B = 20

    def add(self):
        return self.A + self.B

fake = FakeCal()
c1 = sub(5)

print(c1.add1(fake))  # Output: 35 (10 + 20 + 5)
```
This proves that `sub` is not limited to `cal` instances, but works with any compatible object. This is the core of **Duck Typing**.

```python

class cal:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def add(self):
        return self.A + self.B

class sub:
    def __init__(self, C):
        self.C = C

    def add1(self, obj):
        print(obj.add())  # Calls add() from obj
        return obj.A + obj.B + self.C  
        
class FakeCal:
    def __init__(self):
        self.A = 10
        self.B = 20

    def add(self):
        return self.A + self.B

# Create an instance of `cal`
f1 = cal(2, 3)

# Create an instance of `sub`
c1 = sub(5)

# Call add1 method
result = c1.add1(f1)

print(result)  # Output: 10 (2 + 3 + 5)
        

fake = FakeCal()
print(c1.add1(fake))  # Output: 35 (10 + 20 + 5)
```