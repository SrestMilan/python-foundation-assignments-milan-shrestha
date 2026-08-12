"""
Exercise: Dataset Access Decision
Student: Milan Shrestha
Day: 1
"""
# List of roles permitted to access datasets
allowed_roles = ["analyst", "scientist", "engineer"]

# List of datasets that are restricted regardless of role
restricted_datasets = ["salary_data", "personal_data"]


def check_access(scenario_num, user_role, is_active, requested_dataset):
    """Print the scenario header, then determine and print access result."""
    print(f"\nScenario {scenario_num}:")
    # Deny first if the user account is inactive
    if not is_active:
        print("Access denied because the user is inactive.")
    # Deny if the user's role is not in the allowed list
    elif user_role not in allowed_roles:
        print("Access denied because the role is not allowed.")
    # Deny if the requested dataset is restricted, regardless of role
    elif requested_dataset in restricted_datasets:
        print("Access denied because the dataset is restricted.")
    # If none of the above conditions apply, grant access
    else:
        print(f"Access granted to '{requested_dataset}' for role '{user_role}'.")


# Call the function once per scenario — each is a single line
check_access(1, "analyst", True, "sales_data")      # Everything valid
check_access(2, "scientist", False, "sales_data")   # Inactive user
check_access(3, "manager", True, "sales_data")      # Role not allowed
check_access(4, "engineer", True, "salary_data")    # Restricted dataset