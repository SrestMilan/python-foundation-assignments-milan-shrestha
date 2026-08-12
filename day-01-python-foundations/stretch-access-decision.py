"""
Exercise: Dataset Access Decision
Student: Milan Shrestha
Day: 1
"""
# List of roles permitted to access datasets
allowed_roles = ["analyst", "scientist", "engineer"]

# List of datasets that are restricted regardless of role
restricted_datasets = ["salary_data", "personal_data"]


# ---- Scenario 1: Everything valid ----
print("Scenario 1:")
user_role = "analyst"
is_active = True
requested_dataset = "sales_data"

if not is_active:
    print("Access denied because the user is inactive.")
elif user_role not in allowed_roles:
    print("Access denied because the role is not allowed.")
elif requested_dataset in restricted_datasets:
    print("Access denied because the dataset is restricted.")
else:
    print(f"Access granted to '{requested_dataset}' for role '{user_role}'.")


# ---- Scenario 2: Inactive user ----
print("\nScenario 2:")
user_role = "scientist"
is_active = False
requested_dataset = "sales_data"

if not is_active:
    print("Access denied because the user is inactive.")
elif user_role not in allowed_roles:
    print("Access denied because the role is not allowed.")
elif requested_dataset in restricted_datasets:
    print("Access denied because the dataset is restricted.")
else:
    print(f"Access granted to '{requested_dataset}' for role '{user_role}'.")


# ---- Scenario 3: Role not allowed ----
print("\nScenario 3:")
user_role = "manager"
is_active = True
requested_dataset = "sales_data"

if not is_active:
    print("Access denied because the user is inactive.")
elif user_role not in allowed_roles:
    print("Access denied because the role is not allowed.")
elif requested_dataset in restricted_datasets:
    print("Access denied because the dataset is restricted.")
else:
    print(f"Access granted to '{requested_dataset}' for role '{user_role}'.")


# ---- Scenario 4: Restricted dataset ----
print("\nScenario4:")
user_role = "engineer"
is_active = True
requested_dataset = "salary_data"

if not is_active:
    print("Access denied because the user is inactive.")
elif user_role not in allowed_roles:
    print("Access denied because the role is not allowed.")
elif requested_dataset in restricted_datasets:
    print("Access denied because the dataset is restricted.")
else:
    print(f"Access granted to '{requested_dataset}' for role '{user_role}'.")