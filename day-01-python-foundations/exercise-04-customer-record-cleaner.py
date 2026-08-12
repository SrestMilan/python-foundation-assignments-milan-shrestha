
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


def clean_text(value, mode="title"):
    """Strip extra spaces and apply the given case format (title or lower)."""
    value = value.strip()
    return value.title() if mode == "title" else value.lower()


# Clean each field using the helper function
name = clean_text(raw_name, "title")     # e.g. "Sagar Thapa"
city = clean_text(raw_city, "title")     # e.g. "Kathmandu"
email = clean_text(raw_email, "lower")   # emails are conventionally lowercase
age = int(raw_age.strip())               # convert cleaned age to integer

# Ternary expression: if age is 18 or above, status is "Adult", otherwise "Minor"
status = "Adult" if age >= 18 else "Minor"

# Display the cleaned results
print(f"Name: {name}")
print(f"City: {city}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"Status: {status}")