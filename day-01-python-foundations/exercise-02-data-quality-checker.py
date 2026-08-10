# Dataset details
total_rows = 2000
missing_rows = 120
duplicate_rows = 30
labels = ["Excellent", "Acceptable", "Needs Cleaning"]

# Calculate total problematic rows (missing + duplicate, no overlap)
problematic_rows = missing_rows + duplicate_rows

# Calculate problem percentage
problem_percentage = (problematic_rows / total_rows) * 100

# Classify dataset based on problem percentage
if problem_percentage <= 2:
    classification = labels[0]
elif problem_percentage <= 5:
    classification = labels[1]
else:
    classification = labels[2]

# Display the report
print(f"Total Rows          : {total_rows}")
print(f"Problematic Rows    : {problematic_rows}")
print(f"Problem Percentage  : {problem_percentage:.2f}%")
print(f"Final Classification: {classification}")