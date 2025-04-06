# Division Function with Exception Handling in Python

This Python script demonstrates the use of `try`, `except`, and `finally` blocks to handle exceptions, specifically division by zero errors.

## 💡 Functionality

The script defines a function `dev(a, b)` that:

1. Attempts to divide `a` by `b`.
2. Catches a `ZeroDivisionError` or any exception using `except`.
3. Prints a custom error message.
4. Uses a `finally` block to return a message that simulates closing a resource.

## 🧪 Example

```python
def dev(a, b):
    try:
        print("resource open")
        print(a / b)
    except Exception as e:    
        print("you can't divide a number by zero", e)
    finally:
        return "resource closed"

dev1 = dev(2, 0)
print(dev1)
```

### 🔍 Output

```
resource open
you can't divide a number by zero division by zero
resource closed
```

## 📝 Notes

- Even though an exception occurs, the `finally` block always executes.
- Since `finally` returns `"resource closed"`, this overrides any other return or exception.

## 📚 Concepts Covered

- Python exception handling
- `try`, `except`, and `finally` blocks
- Returning values from a function with exception handling


## Example 

``` python

def write_to_file(filename, data):
    file = None
    try:
        print("Opening file...")
        file = open(filename, 'w')
        file.write(data)
        print("Data written successfully!")
    except Exception as e:
        print("An error occurred while writing to the file:", e)
    finally:
        if file:
            file.close()
            print("File closed (resource cleaned up)")
        return "Write operation complete (even if there was an error)"

# Usage
result = write_to_file("sample_output.txt", "Hello, this is a test message!")
print(result)

```

### output:

```
Opening file...
An error occurred while writing to the file: [Errno 13] Permission denied: 'sample_output.txt'
Write operation complete (even if there was an error)

=== Code Execution Successful ===
```
