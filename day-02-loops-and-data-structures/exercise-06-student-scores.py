"""
Exercise: Student Score Dictionary
Student: Milan Shrestha
Day: 2
"""
student_scores = {
    "Anisha": 78,
    "Ravi": 55,
    "Maya": 92,
    "Sagar": 61,
    "Nima": 48
}

# 1. Display each student's name next to their score
for name, marks in student_scores.items():
    print(f"{name}: {marks}")

# 2. Build a new dictionary with only the students who cleared the 60-mark cutoff
passed_students = {name: marks for name, marks in student_scores.items() if marks >= 60}

# 3. Identify the topper — key=lambda compares by marks (item[1]) instead of the default name-based comparison (item[0])
topper_name, topper_marks = max(student_scores.items(), key=lambda item: item[1])

# 4. Work out the class average by dividing total marks by number of students
class_average = sum(student_scores.values()) / len(student_scores)

print(f"\nStudents who passed (60+): {passed_students}")
print(f"Topper: {topper_name} with {topper_marks} marks")
print(f"Class average: {class_average:.2f}")