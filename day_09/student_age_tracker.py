'''from random import choice
from tkinter.font import names

student_information = {}

print("""                    Enter 1 to Add Student
                    Enter 2 to Age of student
                    Enter 3 to Delete student
                    Enter 4 to Edit contact number
                    Enter 5 to View all students
                    Enter 6 to Add subjects marks
                    Enter 7 to identify student marks""")

def add_student(students , name, age, address, contact, student_id):
    students[student_id] = {
        "name" : name,
        "age" : age,
        "address" : address,
        "contact" : contact
    }

def search(students, student_id):
    if student_id in student_information:
        print(f"Student - {student_id} - {students[student_id]}")
    else:
        print(f"Student not found")

def delete_student(student_id,students):
    if student_id in students:
        del students[student_id]
def update_student(students,student_id, updated_no):
    if student_id in student_information:
        students[student_id]["contact"] = updated_no
        print(f"Updated students information - {students[student_id]}")
    else:
        print(f"student not found")
def view_student_name(students):
    for student_id in students.keys():
        print(f"student id {student_id} | student name - {students[student_id]['name']}")

def add_student_marks(students, student_id):
    if student_id in students:
        maths = int(input("Enter marks of Maths: "))
        science = int(input("Enter marks of Science: "))
        history = int(input("Enter marks of history: "))
        #print(students[student_id])
        students[student_id]["marks"] = {
            "maths" : maths,
            "science" : science,
            "history" : history
        }

def view_student_marks(students, student_id):
    if student_id in students:
        if "marks" in students[student_id]:
            print(f"Marks for student - {students[student_id]['name']}")
            for key, val in students[student_id]["marks"].items():
                print(f"Subject - {key} - Marks - {val}")
        else:
            print("Marks are not available for this student")
    else:
        print("Student not found")


def show_student_averages():
    if not student_information:
        print("No student records available.")
        return

    for student_id, student_data in student_information.items():
        if "marks" in student_data:
            total = sum(student_data["marks"].values())
            average = total / len(student_data["marks"])
            print(f"{student_data['name']} - Average Marks: {average:.2f}")
        else:
            print(f"{student_data['name']} - No marks available")


def main():
    choice = input("Please Enter your choice: ")

    if choice == "1":
        student_id = int(input("Enter your id: "))
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        address = input("Enter your address: ")
        contact = input("Enter your contact number: ")
        add_student(students=student_information, age= age,name=name,address=address,contact=contact, student_id=student_id)
        print(student_information)

    elif choice == "2":
        student_id_no = input("Enter id to search: ")
        search(students=student_information, student_id=student_id_no)

    elif choice == "3":
        student_id_no = input("Enter name to delete: ")
        delete_student(students = student_information, student_id=student_id_no)
        print(student_information)

    elif choice == "4":
        student_id = input("Enter student id: ")
        updated_no = input("Please enter updated id no: ")
        update_student(student_information,student_id, updated_no)

    elif choice == "5":
        view_student_name(students=student_information)
    elif choice == "6":
        student_id = int(input("Enter student id: "))
        add_student_marks(student_information, student_id)
    elif choice == "7":
        student_id = int(input("Enter student id: "))
        view_student_marks(students=student_information, student_id=student_id)
    elif choice == "8":
        show_student_averages()

    else:
        print("No name records..")


while True:
    main()'''

# Student Management System

# Stores all student data
student_information = {}

# Menu Display
def show_menu():
    print("""
    ===== Student Management Menu =====
    1. Add Student
    2. Search Student by ID
    3. Delete Student by ID
    4. Update Student Contact Number
    5. View All Student Names
    6. Add Subject Marks for a Student
    7. View Marks of a Student
    8. Show Average Marks for All Students
    9. Exit
    ====================================
    """)

# Add student
def add_student(students, student_id, name, age, address, contact):
    students[student_id] = {
        "name": name,
        "age": age,
        "address": address,
        "contact": contact
    }
    print(f"Student {name} (ID: {student_id}) added successfully.")

# Search student
def search(students, student_id):
    if student_id in students:
        print(f"Student ID: {student_id} -> {students[student_id]}")
    else:
        print("Student not found.")

# Delete student
def delete_student(students, student_id):
    if student_id in students:
        del students[student_id]
        print(f"Student ID {student_id} deleted successfully.")
    else:
        print("Student not found.")

# Update contact
def update_student_contact(students, student_id, updated_no):
    if student_id in students:
        students[student_id]["contact"] = updated_no
        print(f"Contact updated for student {students[student_id]['name']}.")
    else:
        print("Student not found.")

# View student names
def view_student_names(students):
    if not students:
        print("No student records available.")
    else:
        for student_id, details in students.items():
            print(f"ID: {student_id} | Name: {details['name']}")

# Add marks
def add_student_marks(students, student_id):
    if student_id in students:
        maths = int(input("Enter marks for Maths: "))
        science = int(input("Enter marks for Science: "))
        history = int(input("Enter marks for History: "))
        students[student_id]["marks"] = {
            "maths": maths,
            "science": science,
            "history": history
        }
        print("Marks added successfully.")
    else:
        print("Student not found.")

# View marks
def view_student_marks(students, student_id):
    if student_id in students:
        if "marks" in students[student_id]:
            print(f"Marks for {students[student_id]['name']}:")
            for subject, marks in students[student_id]["marks"].items():
                print(f"{subject.capitalize()}: {marks}")
        else:
            print("Marks not available for this student.")
    else:
        print("Student not found.")

# Show averages
def show_student_averages(students):
    if not students:
        print("No student records available.")
        return
    for student_id, student_data in students.items():
        if "marks" in student_data:
            total = sum(student_data["marks"].values())
            average = total / len(student_data["marks"])
            print(f"{student_data['name']} - Average: {average:.2f}")
        else:
            print(f"{student_data['name']} - No marks available.")

# Main loop
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Name: ").strip()
            age = input("Enter Age: ").strip()
            address = input("Enter Address: ").strip()
            contact = input("Enter Contact Number: ").strip()
            add_student(student_information, student_id, name, age, address, contact)

        elif choice == "2":
            student_id = input("Enter Student ID to Search: ").strip()
            search(student_information, student_id)

        elif choice == "3":
            student_id = input("Enter Student ID to Delete: ").strip()
            delete_student(student_information, student_id)

        elif choice == "4":
            student_id = input("Enter Student ID to Update: ").strip()
            updated_no = input("Enter New Contact Number: ").strip()
            update_student_contact(student_information, student_id, updated_no)

        elif choice == "5":
            view_student_names(student_information)

        elif choice == "6":
            student_id = input("Enter Student ID: ").strip()
            add_student_marks(student_information, student_id)

        elif choice == "7":
            student_id = input("Enter Student ID: ").strip()
            view_student_marks(student_information, student_id)

        elif choice == "8":
            show_student_averages(student_information)

        elif choice == "9":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1-9.")

# Run program
main()
