"""
Exercise: File Validator
Student: Milan Shrestha
Day: 1
"""

# Ask the user to enter a file name
file_name = input("Enter a file name: ")

# Remove any leading/trailing spaces and convert to lowercase
# so that comparisons work regardless of how the user types the extension
# (e.g. "CUSTOMERS.JSON" -> "customers.json")
file_name = file_name.strip().lower()

# Check if the file name ends with one of the allowed extensions
if file_name.endswith('.csv'):
    # File is a CSV, so it's valid
    print(f"'{file_name}' is a valid file type.")
elif file_name.endswith('.json'):
    # File is a JSON, so it's valid
    print(f"'{file_name}' is a valid file type.")
elif file_name.endswith('.parquet'):
    # File is a Parquet file, so it's valid
    print(f"'{file_name}' is a valid file type.")
else:
    # File extension didn't match any of the allowed types
    print(f"'{file_name}' is not a valid file type. Please use .csv, .json, or .parquet.")