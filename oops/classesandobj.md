# Student and Course Class Implementation

This Python script demonstrates the implementation of two classes: `Student` and `Course`. It showcases object-oriented programming (OOP) concepts, including instance methods, class methods, and static methods.

## Class: `Student`
The `Student` class represents a student with a name and age. It has the following components:

### Attributes:
- `name`: Stores the student's name.
- `age`: Stores the student's age.

### Methods:
- `__init__(self, name, age)`: Constructor to initialize the student's name and age.
- `display_info(self)`: Prints the student's name and age.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}")
```

## Class: `Course`
The `Course` class represents a course that can have multiple students enrolled up to a maximum limit. It also includes a class-level attribute and static methods.

### Attributes:
- `school`: A class variable set to `"gems"` that represents the school name.
- `name`: Stores the name of the course.
- `max_students`: Defines the maximum number of students allowed in the course.
- `students`: A list that holds `Student` objects enrolled in the course.

### Methods:
- `__init__(self, name, max_students)`: Constructor to initialize the course name, maximum student limit, and an empty list for enrolled students.
- `add_student(self, student)`: Adds a `Student` object to the course if space is available, otherwise, it prints a message stating the course is full.
- `schoolname(cls)`: A class method that returns the value of the class variable `school`.
- `country()`: A static method that returns `"India"`, representing the default country.

```python
class Course:
    school = "gems"
   
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []  # List to hold Student objects

    def add_student(self, student):
        """Adds a Student object to the course if there is space"""
        if len(self.students) < self.max_students:
            self.students.append(student)  # student is the Student object
            print(f"{student.name} has been added to {self.name}.")
        else:
            print(f"Cannot add {student.name}. {self.name} is full.")

    @classmethod
    def schoolname(cls):
        return cls.school
   
    @staticmethod    
    def country():
        return "India"
```

## Example Usage
The script creates instances of the `Student` class and a `Course` instance. It then adds students to the course and demonstrates class and static methods.

### Code Execution:
```python
# Create Student instances
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Create a Course instance
course1 = Course("Math", 2)
print(Course.school)

# Display static and class methods
print(Course.country())    # Output: India
print(Course.schoolname()) # Output: gems

# Add Student objects to the course
course1.add_student(student1)  # Output: Alice has been added to Math.
course1.add_student(student2)  # Output: Bob has been added to Math.
```

## Key OOP Concepts Used:
1. **Instance Variables and Methods** - `Student` and `Course` classes have attributes and methods that operate on instances.
2. **Class Variables and Methods** - `school` is a class variable accessed through a class method.
3. **Static Methods** - `country()` does not depend on any instance or class attribute.
4. **Encapsulation** - The `students` list is managed internally by the `Course` class.

This script is an excellent example of how classes and objects work together in Python, making it useful for beginners learning OOP principles.


```
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}")

class Course:
    school = "gems"
   
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []  # List to hold Student objects

    def add_student(self, student):
        """Adds a Student object to the course if there is space"""
        if len(self.students) < self.max_students:
            self.students.append(student)  # student is the Student object
            print(f"{student.name} has been added to {self.name}.")
        else:
            print(f"Cannot add {student.name}. {self.name} is full.")

    @classmethod
    def schoolname(cls):
        return cls.school
   
    @staticmethod    
    def country():
        return "India"

# Create Student instances
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Create a Course instance
course1 = Course("Math", 2)
print(Course.school)

# Display static and class methods
print(Course.country())    # Output: India
print(Course.schoolname()) # Output: gems

# Add Student objects to the course
course1.add_student(student1)  # Output: Alice has been added to Math.
course1.add_student(student2)  # Output: Bob has been added to Math.
```