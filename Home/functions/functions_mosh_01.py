#parameters - input that you add in functions
#argument - actual value given parameters
# Functions are,
#               1. perform a task
#               2. Return a value

'''def greet():
    print("Hi there")
    print("Hi there")


greet()'''
'''
def hello(first_name, age):
    print(f"hello {first_name},")
    print(f"you are {age} years old.")


hello("samitha", 27 )'''

'''def get_greet(name):
    return f"Hi {name}"

get_greet("samitha")
print(get_greet("samitha"))'''
'''
# keyword arguments
def increment(number, by):
    return number + by

print(increment(2,by=1))
# in here by is the keyword argument - it helps more readble..
'''
'''def increment(number, by=1):
    return number + by

print(increment(2))
# we can use by as optional argument
'''
'''
#arg
# with parameters having * - final code will be tupple
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print(multiply(2,3,4,5))

#**args
def save_user(**user):
    print(user)
    print(user["name"])

save_user(id=1, name="john", age=22)

#scope
message = "a"
def greet(name):
    global message
    message = "b"

greet("mosh")
print(message)'''
'''
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizzbuzz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "buzz"
    return input

print(fizz_buzz(15))'''

'''def els(num,num2):
    total = num * num2
    return total

print(els(3,2))'''

#========================================================
#
# student = {
#     "name" : "samitha",
#     "age" : 27,
#     "grade" : "A",
#     "marks": [23,43,2]
# }
#
# for value in student.values():
#     print(value)
#
# student["name"] = "23111"
#
# student["marks"].append(47)
#
# for value in student.items():
#     print(value)
#
# for marks in student["marks"]:
#     print(marks)

# for key, value in student.items():
#     print(f"key: {key}, value: {value}")


# empty_phonebook = {}
#
# def add_contact(phonebook, name, number):
#     if name not in phonebook:
#         phonebook[name] = number
#         print(f"Contact '{name}' added successfully!")
#     else:
#         print(f"Contact '{name}' already exists! Use update instead.")
#
# def search_contact(phonebook, name):
#     if name in phonebook:
#         return phonebook[name]
#     else:
#         return "Contact not found"
#
# def delete_contact(phonebook, name):
#     if name in phonebook:
#         del phonebook[name]
#         return True
#     else:
#         return False
#
# def update_contact(phonebook, name, number):
#     if name not in phonebook:
#         phonebook[name] = number
#         return True
#     else:
#         return False
#
#
# def main_func():
#     global empty_phonebook
#
#     while True:
#         print("""Main menu:
#                 1. Add a new contact
#                 2. Search a contact
#                 3. Delete a contact
#                 4. Look phone book
#                 5. Update existing contact
#                 6. Exit
#     """)
#
#         try:
#             choice = int(input("Enter your selection: "))
#         except ValueError:
#             print("Please enter a valid number!")
#             continue
#
#         if choice == 1:
#             name = input("Enter contact name: ")
#             number = input("Enter contact number: ")
#
#             add_contact(phonebook=empty_phonebook, name=name, number=number)
#
#         elif choice == 2:
#             name = input("Enter contact name: ")
#             result = search_contact(phonebook=empty_phonebook, name=name)
#             print(f"{name}: {result}")
#
#         elif choice == 3:
#             name = input("Enter contact name: ")
#             if delete_contact(phonebook=empty_phonebook, name=name):
#                 print(f"{name} successfully deleted")
#             else:
#                 print(f"{name} not found")
#
#         elif choice == 4:
#             if empty_phonebook:
#                 for name, number in empty_phonebook.items():
#                     print(f"{name}: {number}")
#             else:
#                 print("Phonebook is empty")
#
#         elif choice == 5:
#             name = input("Enter contact name: ")
#             number = int(input("Enter contact number: "))
#             if update_contact(phonebook=empty_phonebook, name=name, number=number):
#                 print(f"{name} is successfully updated")
#             else:
#                 print(f"{name} not found - cannot update")
#
#         elif choice == 6:
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice! Please select 1-6")
#
# main_func()

# Student Management System

# Stores all student data
# student_information = {}
#
# # Menu Display
# def show_menu():
#     print("""
#     ===== Student Management Menu =====
#     1. Add Student
#     2. Search Student by ID
#     3. Delete Student by ID
#     4. Update Student Contact Number
#     5. View All Student Names
#     6. Add Subject Marks for a Student
#     7. View Marks of a Student
#     8. Show Average Marks for All Students
#     9. Exit
#     ====================================
#     """)
#
# def add_student(students, student_id, name, age, address, contact):
#     students[student_id]={
#         "name": name,
#         "age": age,
#         "address": address,
#         "contact": contact
#     }
#     print(f"{student_id}: {name} successfully added!")
#
# def search_student(students, student_id):
#     if student_id in students:
#         print(f"{students[student_id]}")
#     else:
#         print("Student not found.")
#
#
# def delete_student(students, student_id):
#     if student_id in students:
#         del students[student_id]
#         print(f"{student_id}: deleted!")
#
#
# def update_student_contact(students, student_id, contact_no):
#     if student_id in students:
#         students[student_id]["contact_no"] = contact_no
#     else:
#         print("Student not found.")
#
#
# def main():
#     while True:
#         show_menu()
#
#         input_usr = int(input("Enter your selection: "))
#
#         if input_usr == 1:
#             student_id = input("Student ID: ")
#             name = input("Student Name: ")
#             age = input("Student Age: ")
#             address = input("Student Address: ")
#             contact = input("Student Contact No: ")
#             add_student(student_information, student_id, name, age, address, contact)
#
#         if input_usr == 2:
#             student_id = input("Student ID: ")
#
#             search_student(student_information, student_id)
#
#         if input_usr == 3:
#             student_id = input("Student ID: ")
#
#             delete_student(student_information, student_id)
#
#         if input_usr == 4:
#             student_id = input("Enter Student ID to Update: ").strip()
#             contact_no = input("Enter New Contact Number: ").strip()
#             update_student_contact(student_information, student_id, contact_no)
#
#
#
# main()

