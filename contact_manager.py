# contact_manager.py
# Simple contact saver written for Pydroid 3 / phone or PC
# Stores contacts in memory (list of tuples) while the program runs

contact_details = []  # global list to hold tuples: (name, phone)

def add_contact():
    """Add one or more contacts to contact_details."""
    while True:
        try:
            contact_count = int(input("Enter the number of contacts to save: "))
            if contact_count <= 0:
                print("Enter a positive number!")
                continue
            break
        except ValueError:
            print("Enter a valid integer!")

    for i in range(contact_count):
        contact_name = input(f"Enter contact {i+1} name: ").title().strip()
        while True:
            contact_number = input(f"Enter contact {i+1} phone number: ").strip()
            if contact_number.isdigit() and len(contact_number) == 11:
                print("Contact saved!\n")
                break
            else:
                print("Enter a valid 11 digit phone number!")
        contact_details.append((contact_name, contact_number))
    return contact_details


def view_contacts():
    """Display all saved contacts."""
    if not contact_details:
        print("\nNo contact saved!")
    else:
        print("\nContact List:")
        for i, (contact_name, contact_number) in enumerate(contact_details, start=1):
            print(f"{i}. {contact_name} - {contact_number}")


def search_contact():
    """Search by name or phone number and print result."""
    search_input = input("Enter name or phone number: ").strip()
    # Normalize name searches (but keep number searches as-is)
    search_name = search_input.title()
    found = False

    if not contact_details:
        print("\nNo contact saved!")
        return

    for contact_name, contact_number in contact_details:
        if search_input == contact_number or search_name == contact_name:
            print(f"Contact found: {contact_name} - {contact_number}")
            found = True
            break

    if not found:
        print("No such name or number found!")


def main():
    print("--- Contact Book ---\n")
    name = input("Enter your name: ").title().strip()
    print(f"\nGood day, {name}!\n")

    while True:
        print('''
Choose an option:
1. Add contact
2. View all contacts
3. Search contact
4. Exit
        ''')
        number_choice = input("Option: ").strip()

        if number_choice == "1":
            add_contact()
        elif number_choice == "2":
            view_contacts()
        elif number_choice == "3":
            search_contact()
        elif number_choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid number!")

if __name__ == "__main__":
    main()
