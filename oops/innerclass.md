# Student Class with Inner Section Class

This Python script demonstrates the use of an **inner class** within a `Student` class. The `Section` class is nested inside `Student`, which helps in logical grouping and encapsulation of related attributes.

## Class: `Student`
The `Student` class represents a student with a name, age, and section.

### Attributes:
- `name`: Stores the student's name.
- `age`: Stores the student's age.
- `sec`: An instance of the inner `Section` class.

### Methods:
- `__init__(self, name, age, sec)`: Constructor to initialize the student's name, age, and section.
- `display_info(self)`: Prints the student's name, age, and section.

## Inner Class: `Section`
The `Section` class is defined inside the `Student` class. It manages the section of the student.

### Attributes:
- `sec`: Stores the section of the student.

### Methods:
- `__init__(self, sec)`: Initializes the section attribute.
- `get_sec(self)`: Returns the section of the student.

## Code Implementation:
```python
class Student:
    def __init__(self, name, age, sec):
        self.name = name
        self.age = age
        self.sec = self.Section(sec)
   
    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Section: {self.sec.get_sec()}.")

    class Section:
        def __init__(self, sec):
            self.sec = sec

        def get_sec(self):
            return self.sec

# Example Usage
student1 = Student("Alice", 20, "B")
student1.display_info()

print(Student.Section.get_sec(student1.sec))
```

## Explanation:
1. The `Section` class is an **inner class**, meaning it is defined inside another class (`Student`).
2. `Student` objects create an instance of `Section` when initialized, ensuring that every student has an associated section.
3. The method `display_info()` prints the student's details, including the section retrieved from the inner class.
4. We access the inner class method `get_sec()` through `Student.Section.get_sec(student1.sec)`.

## Benefits of Using an Inner Class:
- **Encapsulation**: Keeps related functionality within the parent class.
- **Logical Grouping**: The `Section` class is only relevant to `Student`, making the code more organized.
- **Readability**: Helps in maintaining a structured approach when dealing with complex objects.

This script is a great example of how to implement and use inner classes in Python effectively!