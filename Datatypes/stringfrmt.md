# Python String Operations Guide

## String Indexing
```python
text = "Hello World"

# Accessing characters
text[0]      # 'H'  - First character
text[4]      # 'o'  - Fifth character
text[-1]     # 'd'  - Last character
text[-2]     # 'l'  - Second to last character

# String length
len(text)    # 11   - Total number of characters including space
```

In Python, string indexing starts at 0. You can also use negative indices to count from the end of the string:
- Positive indices (0 to len-1): Count from the start
- Negative indices (-1 to -len): Count from the end
- len() function returns the total length of the string

## String Slicing
```python
text = "Python Programming"

# Basic slicing: string[start:end:step]
text[0:6]      # "Python"     - Characters from index 0 to 5
text[7:]       # "Programming" - Characters from index 7 to end
text[:6]       # "Python"     - Characters from start to index 5
text[-11:]     # "Programming" - Last 11 characters

# Using step
text[::2]      # "Pto rgamn"  - Every second character
text[::-1]     # "gnimmargorP nohtyP" - Reverse the string

# Negative indices
text[-7:-2]    # "rammi"      - 7th to 3rd characters from end
```

Slicing syntax: `[start:end:step]`
- `start`: First index to include (optional, defaults to 0)
- `end`: First index to exclude (optional, defaults to string length)
- `step`: Number of characters to skip (optional, defaults to 1)

## String Manipulation
```python
# Concatenation
str1 = "Hello"
str2 = "World"
str1 + " " + str2           # "Hello World" - Using + operator
" ".join([str1, str2])      # "Hello World" - Using join method

# String repetition
"Ha" * 3                    # "HaHaHa" - Repeats string 3 times

# f-strings (Python 3.6+)
name = "John"
age = 25
f"Hello, {name}! You are {age} years old."  # "Hello, John! You are 25 years old."

# Case manipulation
"hello".upper()             # "HELLO" - All uppercase
"WORLD".lower()             # "world" - All lowercase
"hello world".title()       # "Hello World" - Capitalize each word
"hello world".capitalize()  # "Hello world" - Capitalize first letter

# Removing whitespace
"  Hello  ".strip()        # "Hello" - Remove spaces from both ends
"  Hello  ".lstrip()       # "Hello  " - Remove spaces from left
"  Hello  ".rstrip()       # "  Hello" - Remove spaces from right
```

## String Methods
```python
sentence = "The quick brown fox jumps over the lazy dog"

# Search methods
sentence.find("fox")        # 16 - Index where 'fox' starts
"fox" in sentence          # True - Check if 'fox' exists
sentence.startswith("The")  # True - Check if starts with 'The'
sentence.endswith("dog")    # True - Check if ends with 'dog'
sentence.count("the")       # 2 - Count occurrences (case sensitive)

# Replace methods
sentence.replace("dog", "cat")      # Replace all 'dog' with 'cat'

sentence = "the quick brown fox the the  jumps over the lazy dog"
new_sentence = sentence.replace("the", "a", 4)
print(new_sentence)  # Output: "a quick brown fox a a  jumps over a lazy dog


# Split and Joins
words = sentence.split()    # Split into list of words
print(words)               # ['The', 'quick', 'brown', 'fox', ...]
" ".join(words)            # Join words back with spaces

# Case checking
"Hello".isupper()         # False - Not all uppercase
"HELLO".isupper()         # True - All uppercase
"hello".islower()         # True - All lowercase
"Hello123".isalnum()      # True - All alphanumeric
"Hello".isalpha()         # True - All alphabetic
"123".isdigit()           # True - All digits

```

## Common Use Cases
```python
# String formatting
name = "Alice"
age = 25
# Using format method
"Name: {}, Age: {}".format(name, age)    # "Name: Alice, Age: 25"
# Using f-strings (Python 3.6+)
f"Name: {name}, Age: {age}"              # "Name: Alice, Age: 25"

# Substring checking
text = "Python Programming"
"Python" in text           # True - Check substring existence
text = "Python Programming"
print(text.find("gram"))       
        
text = "Python Programming"
print(text.index("graam"))       # 8 - Find index (raises error if not found)


# String validation
"123".isdigit()           # True - Contains only digits
"abc123".isalnum()        # True - Contains letters/numbers
"   ".isspace()           # True - Contains only whitespace
print("hello".isalpha())       # True  - Only alphabets

```
