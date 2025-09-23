empty_phonebook = {}

def add_to_contact_list(phone_book,user_name,phone_number):
    if user_name not in phone_book:
        phone_book[user_name] = phone_number
    else:
        phone_book[user_name].append(user_name)

def search_list(phone_book,name):
    return phone_book[name]

def delete_contact(phone_book,contact_name):
    if contact_name in phone_book:
        del phone_book[contact_name]

def main_func():
    global empty_phonebook


    print("""Main menu:
            1. Add a new contact ( press 1 ) 
            2. Search a contact ( press 2 )
            3. Delete a contact ( press 3 ) 
            4. Look phone book ( press 4 )
            5. Update existing contact ( press 5 )
""")

    choice = int(input("Enter your selection: "))

    if  choice == 1:
        print("---/----/----/---/---")
        name = input("\nEnter a contact name: ")
        number = int(input("Enter phone number: "))

        add_to_contact_list(phone_book=empty_phonebook,user_name=name,phone_number=number)
        print(empty_phonebook)

    elif choice == 2:
        print("---/----/----/---/---\n")
        search_input = str(input("Enter name (strings): "))

        if search_input in empty_phonebook:
            print(f"{search_input}'s number is {search_list(phone_book=empty_phonebook,name=search_input)} ")

    elif choice == 3:
        print("---/----/----/---/---\n")
        delete_input = str(input("Enter name: "))
        if delete_input in empty_phonebook:
            delete_contact(phone_book=empty_phonebook,contact_name=delete_input)

    elif choice == 4:
        print("---/----/----/---/---\n")
        print(empty_phonebook)

    elif choice == 5:
        name =  input("enter name to add another number: ")
        add_to_contact_list(phone_book=empty_phonebook, user_name=name, phone_number = number)
        print()

while True:
    main_func()
