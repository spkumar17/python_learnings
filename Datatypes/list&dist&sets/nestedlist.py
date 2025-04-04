# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example

# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

# alpha
# beta
# Input Format

# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints

# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry
# Explanation 0

# There are  students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.




# Get the number of students
num_students = int(input("Enter the number of students: "))
if 2 <= num_students and num_students  <= 5:
    # List to store student records
    name_marks = []

# Collect student data
    for i in range(num_students):
        name = input("Enter the name of student: ")
        marks = float(input("Enter the number of marks: "))
        name_marks.append([name, marks])  # Store name and marks as a list

# Find highest score
    highscore = 0
    for record in name_marks:
        marks = record[1]  # Extract marks
        if marks > highscore:
            highscore = marks

    print("Highest Score:", highscore)
    second_high = 0
    for record in name_marks:
        marks = record[1]
        if marks == highscore:
            continue 
        elif marks > second_high:
            second_high = marks
    print("second highest score: ", second_high)

    second_high_name = []
    for record in name_marks:
        if record[1] == second_high:
            second_high_name.append(record[0])
    print("list of second high students",second_high_name)   
    second_high_name.sort()


    for output in second_high_name:
        print(str(output))
else:
    print("print a valid student number in range (2 <= student <= 5) ")

        
    
        