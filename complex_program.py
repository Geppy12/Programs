# Student Grade Calculator

print("=== Student Grade Calculator ===")

# Get user input
student_name = input("Enter the student's name: ")
assignment1 = float(input("Enter Assignment 1 grade: "))
assignment2 = float(input("Enter Assignment 2 grade: "))
quiz = float(input("Enter Quiz grade: "))
exam = float(input("Enter Exam grade: "))

# Calculate the average
average = (assignment1 + assignment2 + quiz + exam) / 4

# Determine pass or fail
if average >= 70:
    result = "PASS"
else:
    result = "FAIL"

# Display results
print("\n----- Student Report -----")
print("Student:", student_name)
print("Assignment 1:", assignment1)
print("Assignment 2:", assignment2)
print("Quiz:", quiz)
print("Exam:", exam)
print("Average:", round(average, 2))
print("Result:", result)
print("--------------------------")