class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name not in self.contacts:
            self.contacts[name] = {'Phone': phone, 'Email': email}
            print(f'Contact {name} added successfully.')
        else:
            print(f'Contact {name} already exists.')

    def view_all_contacts(self):
        if self.contacts:
            print("All Contacts:")
            for name, info in self.contacts.items():
                print(f'{name}: Phone - {info["Phone"]}, Email - {info["Email"]}')
        else:
            print("No contacts found.")

    def search_contact(self, name):
        if name in self.contacts:
            info = self.contacts[name]
            print(f'Contact Information for {name}: Phone - {info["Phone"]}, Email - {info["Email"]}')
        else:
            print(f'Contact {name} not found.')

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f'Contact {name} deleted successfully.')
        else:
            print(f'Contact {name} not found.')

# Function to get user input for adding a contact
def get_user_input_add():
    name = input("Enter the contact name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    return name, phone, email

# Function to get user input for searching or deleting a contact
def get_user_input_search_delete():
    name = input("Enter the contact name: ")
    return name

# Example Usage:
contact_book = ContactBook()

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name, phone, email = get_user_input_add()
        contact_book.add_contact(name, phone, email)
    elif choice == '2':
        contact_book.view_all_contacts()
    elif choice == '3':
        name = get_user_input_search_delete()
        contact_book.search_contact(name)
    elif choice == '4':
        name = get_user_input_search_delete()
        contact_book.delete_contact(name)
    elif choice == '5':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
