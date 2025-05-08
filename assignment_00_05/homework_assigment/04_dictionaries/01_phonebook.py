#Problem Statement
#In this program we show an example of using dictionaries to keep track of
#information in a phonebook.

def display_menu():
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Exit")

def main():
    phonebook = {}

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            number = input("Enter phone number: ")
            phonebook[name] = number
            print(f"{name} added to phonebook.")

        elif choice == '2':
            name = input("Enter name to search: ")
            if name in phonebook:
                print(f"{name}'s number is {phonebook[name]}")
            else:
                print(f"{name} not found in phonebook.")

        elif choice == '3':
            name = input("Enter name to delete: ")
            if name in phonebook:
                del phonebook[name]
                print(f"{name} deleted from phonebook.")
            else:
                print(f"{name} not found in phonebook.")

        elif choice == '4':
            if phonebook:
                print("\nContacts in Phonebook:")
                for name, number in phonebook.items():
                    print(f"{name}: {number}")
            else:
                print("Phonebook is empty.")

        elif choice == '5':
            print("Exiting phonebook. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
