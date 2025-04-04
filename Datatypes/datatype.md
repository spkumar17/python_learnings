# Python List, Tuple, and Dictionary Operations Examples

This repository contains examples of various Python data structure operations, demonstrating common methods and iterations.

## List Operations

### Basic List Operations
```python
nums = [12, 23, 34, 45, 12]

# Check type
print(type(nums))  # <class 'list'>

# Get indices
ini = []
for i in nums:
    ini.append(nums.index(i))
print(ini)  # [0, 1, 2, 3, 0]

# Index and Count
print(nums.index(12))  # 0 (first occurrence)
print(nums.count(12))  # 2 (number of occurrences)
```

### List Modifications
```python
nums = [12, 23, 34, 45, 12]

# Pop and Insert
print(nums.pop(0))  # 12
nums.insert(3, 9)
print(nums)  # [23, 34, 45, 9, 12]

# Remove Element
nums.remove(34)
print(nums)  # [23, 45, 9, 12]

# Sort and Reverse
nums.sort()
print(nums)  # [9, 12, 23, 45]
nums.reverse()
print(nums)  # [45, 23, 12, 9]

# Copy and Sum
x = nums.copy()
print(x)  # [45, 23, 12, 9]
sumx = sum(x)
print(sumx)  # 89

# Clear List
nums.clear()
print(nums)  # []
```

### List Iterations
```python
nums = [12, 23, 34, 45, 12]

# Nested Loop for Pairs
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        print(nums[i], nums[j])

# Find Maximum Sum of Adjacent Elements
nums = [12, 23, 34, 45, 12]
add = 0
large = 0
for i in range(len(nums)-1):
    add = nums[i] + nums[i+1]
    large = max(add, large)
print(large)  # 79 (45 + 34)
```

## Tuple and Set Operations
```python
tup = (12, 23, 53, 75, 12, 23)

# Tuple Methods
print(tup.count(12))  # 2
print(tup.index(23))  # 1

# Convert Tuple to Set
lis = set(tup)
print(lis)  # {12, 23, 53, 75}
```

## Dictionary Operations
```python
# Basic Dictionary Creation and Access
data = {1: "naveen", 2: "praveen", 3: "kiran"}
print(data[1])  # naveen

# Creating Dictionary from Lists
keys = ["kumar", "harish", "Srinivas"]
values = ["java", "python", "css"]
mix = dict(zip(keys, values))
print(mix)  # {'kumar': 'java', 'harish': 'python', 'Srinivas': 'css'}

# Dictionary Methods
dub = mix.copy()  # Create a copy
print(dub)  # {'kumar': 'java', 'harish': 'python', 'Srinivas': 'css'}

# Items, Keys, and Values
print(mix.items())  # dict_items([('kumar', 'java'), ('harish', 'python'), ('Srinivas', 'css')])
print(list(mix.items()))  # [('kumar', 'java'), ('harish', 'python'), ('Srinivas', 'css')]
print(list(mix.keys()))  # ['kumar', 'harish', 'Srinivas']

# Pop and Remove
print(mix.pop("kumar"))  # java
print(mix)  # {'harish': 'python', 'Srinivas': 'css'}

# Create Dictionary with Default Values
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # {'a': 0, 'b': 0, 'c': 0}
print(new_dict.keys())  # dict_keys(['a', 'b', 'c'])
print(new_dict.values())  # dict_values([0, 0, 0])

# PopItem and SetDefault
print(new_dict.popitem())  # ('c', 0)
print(new_dict.setdefault("d", 1))  # 1
print(new_dict)  # {'a': 0, 'b': 0, 'd': 1}

# Update Dictionary
new_dict.update({"city": "New York", "age": 26})
print(new_dict)  # {'a': 0, 'b': 0, 'd': 1, 'city': 'New York', 'age': 26}

# Get Method with Default Value
print(mix.get("kumar", "Not Found"))  # Not Found
print(mix.get("harish", "Not Found"))  # python
```

## Key Concepts Demonstrated
- List methods: index(), count(), pop(), insert(), remove(), sort(), reverse(), copy(), clear()
- List iterations and nested loops
- Finding maximum sum of adjacent elements
- Tuple methods: count(), index()
- Converting tuple to set for unique elements
- Dictionary methods: copy(), items(), keys(), values(), pop(), popitem(), setdefault(), update(), get()
- Creating dictionaries from lists using zip()
- Dictionary comprehension and default values

# Python Multiple Return Values Guide

A comprehensive guide demonstrating how Python functions can return multiple values.

## Basic Usage

Python functions can return multiple values as a tuple:

```python
def person(name, *data):
    print(name)
    print(data)
    return name, data

k = person("kumar", 23, "mumbai", 34)
print("Returned value:", k)
```

Output:
```
kumar
(23, 'mumbai', 34)
Returned value: ('kumar', (23, 'mumbai', 34))
```

## Unpacking Values

You can unpack returned values into separate variables:

```python
name, data = person("kumar", 23, "mumbai", 34)
print(name)  # Output: kumar
print(data)  # Output: (23, 'mumbai', 34)
```

## Converting to List

Convert tuple data to a list:

```python
print("Return additional values", list(data))
# Output: Return additional values [23, 'mumbai', 34]
```

## Using Keyword Arguments

Python functions can accept and return keyword arguments using `**kwargs`:

```python
def person(name, **data):
    return name, data  # Returns name and data as a tuple

# Using keyword arguments
name, data = person("kumar", Age=23, City="mumbai")
print("Return name:", name)

# Iterating over the dictionary
for key, value in data.items():  # Note: Must use .items()
    print("additional data:", key, "=>", value)
```

Output:
```
Return name: kumar
additional data: Age => 23
additional data: City => mumbai
```

### Common Pitfalls
❌ Incorrect way (causes error):
```python
for key, value in data.items:  # Missing parentheses
    print("additional data:", key, "=>", value)
```

✅ Correct way:
```python
for key, value in data.items():  # Using parentheses
    print("additional data:", key, "=>", value)
```

## Key Points
- Multiple return values are automatically packed into a tuple
- Use tuple unpacking to extract values separately
- Convert tuple data to list using `list()`
- `**kwargs` stores keyword arguments as a dictionary
- Always use `.items()` (with parentheses) to iterate over dictionary key-value pairs


#------------------------------------------------------

# Python Programming Guide

A comprehensive guide demonstrating key Python concepts including multiple return values and global variables.


## Global Variables

### Using global Keyword

The `global` keyword allows a function to modify a global variable inside its scope:

```python
a = 10

def num():
    global a  # Declaring 'a' as a global variable
    a = 2     # Modifying the global 'a'
    print("in fun", a)

num()
print("outside", a)
```

Output:
```
in fun 2
outside 2
```

Without `global`, assigning a value to a variable inside a function creates a local variable instead of modifying the global one.

### Using globals() Function

The `globals()` function returns a dictionary of all global variables:

```python
a = 10
b = 12
c = 2

def num():
    global a
    a = 2  # Modifying the global 'a'
    x = globals()["b"]  # Accessing 'b' dynamically from the global scope
    print("in fun", x)

num()
print("outside", a)
```

Output:
```
in fun 12
outside 2
```

### Comparison

Feature comparison between `global` and `globals()`:

| Feature | Using `global` | Using `globals()` |
|---------|---------------|-------------------|
| Modifying Global Variables | ✅ Yes (direct modification) | ❌ No (only access, unless explicitly modified) |
| Accessing Other Global Variables | ❌ No | ✅ Yes (via dictionary lookup) |
| Performance | 🚀 Faster | 🐢 Slightly slower (dictionary lookup) |
| Readability | ✅ More readable | ⚠️ Less readable |

## Key Points
- Multiple return values are automatically packed into a tuple
- Use tuple unpacking to extract values separately
- Convert tuple data to list using `list()`
- `**kwargs` stores keyword arguments as a dictionary
- Always use `.items()` (with parentheses) to iterate over dictionary key-value pairs
- Use `global` when modifying a global variable inside a function
- Use `globals()["var"]` when you need to dynamically access a global variable
- Direct access is faster and more readable than `globals()` unless dynamic access is required
#------------------------------------------------------

**Python Notes: Functional Programming and Algorithms**

---

## **1. Using `filter()`, `map()`, and `reduce()`**

### **Filtering Even Numbers**
```python
from functools import reduce

lst = [4, 23, 9, 55, 6, 3, 6, 7, 7, 89]

Even = list(filter(lambda a: a % 2 == 0, lst))
print("Even numbers:", Even)  # Output: [4, 6, 6]
```
### **Doubling the Even Numbers using `map()`**
```python
double = list(map(lambda a: a * 2, Even))
print("Doubled even numbers:", double)  # Output: [8, 12, 12]
```
### **Summing the Doubled Even Numbers using `reduce()`**
```python
add = reduce(lambda a, b: a + b, double)
print("Sum of doubles", add)  # Output: 32
```

---

## **2. Calculating Factorial Using Recursion**
```python
n = int(input("Enter the factorial:"))
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

result = fact(n)
print(f"Factorial of {n} is {result}")
```

---

## **3. Calculating Factorial Using Iteration**
```python
n = int(input("Enter the factorial:"))
def fact(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = i * factorial
    return factorial

result = fact(n)
print(f"Factorial of {n} is {result}")
```

---

## **4. Fibonacci Series Generation**
```python
n = int(input("Enter the number:"))
def check(n):
    a = 0
    b = 1
    lst = [0, 1]
    if n == 1:
        return lst
    else:
        for i in range(n):
            c = a + b
            a = b
            b = c
            lst.append(c)
        return lst

lst = check(n)
print(f"List of Fibonacci series up to {n} values is {lst}")
```

---

## **5. Counting Even and Odd Numbers in a List**
```python
lst = [12, 23, 343, 55, 121, 112, 34]

def check(lst):
    even_count = 0
    odd_count = 0
    for i in lst:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

even, odd = check(lst)
print(f"List contains {even} even and {odd} odd numbers")
```

---

## **Functional Programming Concepts**

### **1. Lambda Function (Anonymous Function)**
A lambda function is a small anonymous function that can have any number of arguments but only one expression.

### **2. filter() – Filtering Elements from an Iterable**
The filter() function is used to filter elements from a list (or any iterable) based on a condition.

### **3. map() – Apply a Function to Each Element**
The map() function applies a given function to all elements in an iterable.

### **4. reduce() – Reduce an Iterable to a Single Value**
The reduce() function from the functools module reduces an iterable to a single value by applying a function cumulatively.

| Function | Purpose |
|----------|---------|
| Lambda | Create small anonymous functions inline. |
| filter() | Filter elements based on a condition. |
| map() | Apply a function to each element in an iterable. |
| reduce() | Reduce an iterable to a single value. |

---

### **Summary:**
✅ `filter()` extracts elements based on a condition.
✅ `map()` transforms elements of a list.
✅ `reduce()` accumulates values.
✅ Recursion and iteration can be used to calculate factorials.
✅ Fibonacci sequence generation using loops.
✅ Counting even and odd numbers in a list.

🚀 *These concepts are fundamental for functional programming in Python!*

#------------------------------------------------------
# Understanding Python Decorators - Example and Breakdown

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

### Key Takeaway

Calling `add(3, 5)` **does NOT call ****`my_decorator(add)`**** again**—that happened once when Python processed `@my_decorator`. Instead, it calls `wrapper(3, 5)`, which executes the original `add` function inside it (`func(*args, **kwargs)`). 🚀

