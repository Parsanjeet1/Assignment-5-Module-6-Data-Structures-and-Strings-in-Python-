# Task 1: Dictionary of student marks

# Create dictionary
student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eve": 88
}

# Get input from user
name = input("Enter the student's name: ")

# Retrieve and print marks
if name in student_marks:
    print(f"{name}'s marks are: {student_marks[name]}")
else:
    print(f"Student '{name}' not found in the record.")
