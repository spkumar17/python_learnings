# Student Class with Inner Section Class

## Overview
This Python program defines a `Student` class that contains an **inner class** called `Section`. The purpose of the inner class is to store and manage the section of a student separately while keeping it encapsulated within the `Student` class.

## Code Explanation

### **1. Outer Class: `Student`**
The `Student` class represents a student with the following attributes:
- `name`: The name of the student.
- `age`: The age of the student.
- `section`: An instance of the inner `Section` class.

It also includes a method:
- `display_info()`: Prints the student's name, age, and section.

### **2. Inner Class: `Section`**
The `Section` class is defined inside `Student` and has:
- `section`: An attribute to store the section.
- `get_sec()`: A method to return the section value.

## Code
```python
class Student:
    def __init__(self, name, age, section):
        self.name = name
        self.age = age
        self.section = self.Section(section)  # Creating an instance of inner class

    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Section: {self.section.get_sec()}.")

    class Section:
        def __init__(self, section):
            self.section = section

        def get_sec(self):
            return self.section

# Creating a Student object
student1 = Student("Alice", 20, "B")
student1.display_info()

# Accessing the inner class method
print(Student.Section.get_sec(student1.section))
```

## **How It Works**
1. **Creating a Student Instance**:
   ```python
   student1 = Student("Alice", 20, "B")
   ```
   - Creates an instance of `Student`.
   - The `section` attribute is set using the `Section` inner class.

2. **Displaying Student Info**:
   ```python
   student1.display_info()
   ```
   - Calls `display_info()` which prints the student's details.

3. **Accessing Section Data**:
   ```python
   print(Student.Section.get_sec(student1.section))
   ```
   - Calls `get_sec()` on the `section` instance to retrieve the section name.

## **Expected Output**
```
Student Name: Alice, Age: 20, Section: B.
B
```

## **Why Use an Inner Class?**
- Encapsulation: The `Section` class is tightly coupled with `Student`, making it clear that sections are a property of students.
- Organization: Keeps related functionality together, avoiding clutter in the outer class.

## **Alternative Approach**
If an inner class is not needed, we could define `Section` as a separate class:
```python
class Section:
    def __init__(self, section):
        self.section = section

    def get_sec(self):
        return self.section

class Student:
    def __init__(self, name, age, section):
        self.name = name
        self.age = age
        self.section = Section(section)
```
This approach provides more flexibility if `Section` needs to be used independently.

## **Conclusion**
Using an inner class in this example helps encapsulate the section details within the `Student` class. This is useful when a class's data should not be exposed globally but only within its parent class.