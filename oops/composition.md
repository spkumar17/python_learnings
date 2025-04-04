# Composition in Python

## **Overview**
Composition is a design principle in object-oriented programming where a class contains an instance of another class rather than inheriting from it. This enables code reuse without enforcing strict relationships between classes.

## **Example: Composition in Python**
```python
class cal:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def add(self):
        return self.A + self.B

class sub:
    def __init__(self, C, obj):
        self.C = C
        self.obj = obj  # Composition: sub contains a cal instance

    def add1(self):
        return self.obj.A + self.obj.B + self.C  

# Create an instance of `cal`
f1 = cal(2, 3)

# Create an instance of `sub`, passing `f1` (composition)
c1 = sub(5, f1)

# Call add1 method
result = c1.add1()

print(result)  # Output: 10 (2 + 3 + 5)
```

## **Explanation**
1. **Class `cal`**:
   - Has attributes `A` and `B`.
   - Defines `add()` to return the sum of `A` and `B`.

2. **Class `sub`**:
   - Stores an integer `C` and an instance of `cal`.
   - Uses `self.obj` to access the `cal` instance’s data.
   - `add1()` accesses `A` and `B` from `self.obj` and adds `C`.

3. **Object Creation**:
   - `f1 = cal(2, 3)`: Creates an instance of `cal`.
   - `c1 = sub(5, f1)`: Creates `sub`, passing `f1` as an argument.
   - `c1.add1()`: Computes `2 + 3 + 5 = 10`.

## **Why is this Composition?**
- **"Has-A" Relationship:** `sub` **has-a** `cal` instance.
- **No Inheritance:** `sub` does not inherit from `cal` but reuses its attributes and methods.
- **Flexibility:** `cal` and `sub` are independent; we can replace `cal` with another class having the same interface without modifying `sub`.

## **Comparison with Inheritance**
| Feature            | Composition                                  | Inheritance                                  |
|-------------------|--------------------------------|--------------------------------|
| Relationship     | Has-a (uses an instance of another class) | Is-a (inherits from another class) |
| Flexibility      | More flexible; allows changing behavior at runtime | Less flexible; enforces a strict relationship |
| Code Reusability | Uses objects to access functionality | Extends and overrides methods |

### **Conclusion**
Composition is a powerful alternative to inheritance when designing object-oriented systems. It promotes better modularity, reduces tight coupling, and increases reusability.

---
🚀 **Key Takeaway:** If a class "has-a" relationship with another, prefer composition over inheritance for greater flexibility and maintainability!

