# 1. Creating a List:
# You can create a list with square brackets [], and lists can contain different data types.

# Creating a list of integers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ["apple", "banana", "cherry"]

# Mixed data types in a list
mixed_list = [1, "apple", 3.14, True]

print(numbers)     # Outputs: [1, 2, 3, 4, 5]
print(fruits)      # Outputs: ['apple', 'banana', 'cherry']
print(mixed_list)  # Outputs: [1, 'apple', 3.14, True]


# 2. Accessing List Elements (Indexing):
# You can access list elements using their index (starting from 0).
# Accessing individual elements
print(fruits[0])  # Outputs: 'apple'
print(fruits[-1])  # Outputs: 'cherry' (negative index accesses the last element)


# 3. List Slicing:
# You can slice lists to access sublists.
# Slicing lists
print(fruits[0:2])  # Outputs: ['apple', 'banana'] (from index 0 to 1)
print(fruits[::2])  # Outputs: ['apple', 'cherry'] (every second element)


# 4. Modifying List Elements:
# You can change values in a list by reassigning to a specific index.

# Modifying an element
fruits[1] = "blueberry"
print(fruits)  # Outputs: ['apple', 'blueberry', 'cherry']


# 5. Adding Elements to a List:
# You can use append(), insert(), and extend() to add elements to a list.


# Using append() to add an element to the end
fruits.append("orange")
print(fruits)  # Outputs: ['apple', 'blueberry', 'cherry', 'orange']

# Using insert() to add an element at a specific position
fruits.insert(1, "mango")
print(fruits)  # Outputs: ['apple', 'mango', 'blueberry', 'cherry', 'orange']

# Using extend() to add multiple elements
fruits.extend(["grape", "pineapple"])
print(fruits)  # Outputs: ['apple', 'mango', 'blueberry', 'cherry', 'orange', 'grape', 'pineapple']


# 6. Removing Elements from a List:
# You can remove elements with remove(), pop(), or del.


# Using remove() to remove a specific element
fruits.remove("cherry")
print(fruits)  # Outputs: ['apple', 'mango', 'blueberry', 'orange', 'grape', 'pineapple']

# Using pop() to remove an element by index
fruits.pop(0)
print(fruits)

# Using del to remove an element by index
del fruits[2]
print(fruits)  # Outputs: ['mango', 'blueberry', 'grape', 'pineapple']


# 7. List Operations:
# You can perform different operations on lists.


# Checking length of the list
print(len(fruits))

# Concatenating two lists
more_fruits = ["kiwi", "watermelon"]
all_fruits = fruits + more_fruits
print(all_fruits)  # Outputs: ['mango', 'blueberry', 'grape', 'pineapple', 'kiwi', 'watermelon']

# Repeating elements in a list
repeated_list = [1, 2] * 3
print(repeated_list)  # Outputs: [1, 2, 1, 2, 1, 2]



# 8. Sorting a List:
# You can sort lists with sort() 

# Sorting a list in ascending order
numbers = [5, 3, 1, 4, 2]
numbers.sort()
print(numbers)  # Outputs: [1, 2, 3, 4, 5]

# Sorting a list in descending order
numbers.sort(reverse=True)
print(numbers)  # Outputs: [5, 4, 3, 2, 1]



# 9. Copying a List:
# You can copy a list using copy() or slicing.


# Copying a list
copy_of_fruits = fruits.copy()
print(copy_of_fruits)  # Outputs a copy of the fruits list

# Using slicing to copy
copy_of_fruits_slice = fruits[:]
print(copy_of_fruits_slice)  # Outputs a copy of the fruits list