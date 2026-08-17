"""
Exercise: Contact Book Menu
Student: Milan Shrestha
Day: 2
"""
contact_book = {}  # stores all contacts as nested dictionaries, keyed by name

MAIN_MENU = """
1. Add contact
2. Search contact
3. Delete contact
4. Display all contacts
5. Exit
"""

while True:
    print(MAIN_MENU)
    user_choice = input("Enter your choice (1-5): ").strip()

    # --- 1. Add contact ---
    if user_choice == "1":
        contact_name = input("Enter name: ").strip()
        contact_phone = input("Enter phone number: ").strip()
        contact_email = input("Enter email address: ").strip()

        # Nested dictionary — each contact stores its own phone and email under its name
        contact_book[contact_name] = {
            "phone": contact_phone,
            "email": contact_email
        }
        print(f"Contact '{contact_name}' added successfully.")

    # --- 2. Search contact ---
    elif user_choice == "2":
        search_name = input("Enter name to search: ").strip()

        # `in` check avoids a KeyError crash if the name isn't in contact_book
        if search_name in contact_book:
            found_contact = contact_book[search_name]
            print(f"Name: {search_name}")
            print(f"Phone: {found_contact['phone']}")
            print(f"Email: {found_contact['email']}")
        else:
            print(f"No contact found with the name '{search_name}'.")

    # --- 3. Delete contact ---
    elif user_choice == "3":
        delete_name = input("Enter name to delete: ").strip()

        # Same safe-check pattern as search — prevents crashing on a missing key
        if delete_name in contact_book:
            del contact_book[delete_name]
            print(f"Contact '{delete_name}' deleted successfully.")
        else:
            print(f"No contact found with the name '{delete_name}'.")

    # --- 4. Display all contacts ---
    elif user_choice == "4":
        if not contact_book:  # empty dictionary is falsy — cleaner than checking len() == 0
            print("No contacts saved yet.")
        else:
            print("All contacts:")
            for name, info in contact_book.items():
                print(f"- {name}: {info['phone']}, {info['email']}")

    # --- 5. Exit ---
    elif user_choice == "5":
        print("Exiting contact book. Goodbye!")
        break  # stops the while loop, ending the program

    # --- Invalid input handling ---
    else:
        print("Invalid choice. Please select a number between 1 and 5.")