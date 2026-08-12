
"""
Exercise: Customer Record Cleaner
Student: Milan Shrestha
Day: 1
"""

# Raw (messy) input values
raw_name = "  sAgar THAPA "
raw_city = "kATHMANDU "
raw_age = "27"
raw_email = " SAGAR@MAIL.COM "

# Clean the name: remove extra spaces and convert to Title Case (e.g. "Sagar Thapa")
name = raw_name.strip().title()

# Clean the city: remove extra spaces and convert to Title Case (e.g. "Kathmandu")
city = raw_city.strip().title()

# Clean the age: remove extra spaces and convert to an integer for comparison
age = int(raw_age.strip())

# Clean the email: remove extra spaces and convert to lowercase (emails are conventionally lowercase)
email = raw_email.strip().lower()

# Ternary expression: if age is 18 or above, status is "Adult", otherwise "Minor"
status = "Adult" if age >= 18 else "Minor"

# Display the cleaned results
print(f"Name: {name}")
print(f"City: {city}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"Status: {status}")