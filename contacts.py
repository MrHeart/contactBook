# Define a Contact class to represent individual contacts
class Contact:
    def __init__(self, fullname, phone_number):
        self.fullname = fullname
        self.phone_number = phone_number

# Define a ContactsBook class to manage contacts
class ContactsBook:
    def __init__(self):
        self.contacts = []

    # Method to add a new contact
    def add_contact(self, fullname, phone_number):
        contact = Contact(fullname, phone_number)
        self.contacts.append(contact)

    # Method to delete a contact by name
    def delete_contact(self, fullname):
        for contact in self.contacts:
            if contact.fullname == fullname:
                self.contacts.remove(contact)
                return True
        return False

    # Method to display all contacts in a tabular form
    def display_contacts(self):
        
        print("\nContacts:")
        if not self.contacts:
            print("No contacts found.")
        else:
            print("{:<30} {:<15}".format("Full Name", "Phone Number"))
            print("-" * 45)
            for contact in self.contacts:
                print("{:<30} {:<15}".format(contact.fullname, contact.phone_number))

    # Method to perform Quick Sort on contacts by name
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x.fullname < pivot.fullname]
        middle = [x for x in arr if x.fullname == pivot.fullname]
        right = [x for x in arr if x.fullname > pivot.fullname]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    # Method to sort contacts by name
    def sort_contacts(self):
        self.contacts = self.quick_sort(self.contacts)
        print("Contacts sorted by name!")

    # Method to perform Binary Search for a contact by name
    def binary_search(self, query):
        left, right = 0, len(self.contacts) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.contacts[mid].fullname.lower() == query.lower():
                return self.contacts[mid]
            elif self.contacts[mid].fullname.lower() < query.lower():
                left = mid + 1
            else:
                right = mid - 1
        return None

# Main function to run the contacts book program
def main():
    contacts_book = ContactsBook()

    while True:
        print("\nContacts Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Sort Contacts")
        print("4. Search Contact")
        print("5. Display Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            fullname = input("Enter full name: ")
            phone_number = input("Enter phone number: ")
            contacts_book.add_contact(fullname, phone_number)
            print("Contact added!")

        elif choice == "2":
            fullname = input("Enter full name to delete: ")
            if contacts_book.delete_contact(fullname):
                print("Contact deleted!")
            else:
                print("Contact not found!")

        elif choice == "3":
            contacts_book.sort_contacts()

        elif choice == "4":
            query = input("Enter a name to search: ")
            contact = contacts_book.binary_search(query)
            if contact:
                print("Search result:")
                print("{:<30} {:<15}".format(contact.fullname, contact.phone_number))
            else:
                print("No matching contact found!")

        elif choice == "5":
            contacts_book.sort_contacts()
            contacts_book.display_contacts()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
