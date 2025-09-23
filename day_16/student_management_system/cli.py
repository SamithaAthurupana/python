# student_management_system/cli.py

from student_management_system.repositories import StudentRepository
from student_management_system.service import StudentService

def show_menu():
    print("""
    ===== Student Management Menu =====
    1. Add Student
    2. Search Student by ID
    3. Delete Student by ID
    4. Update Student Contact Number
    5. View All Students
    6. Add Subject Marks
    7. View Student Marks
    8. Show Average Marks
    9. Exit
    ===================================
    """)

def main():
    repo = StudentRepository()
    service = StudentService(repo)

    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            first_name = input("Enter First Name: ").strip()
            last_name = input("Enter Last Name: ").strip()
            address = input("Enter Address: ").strip()
            nic = input("Enter NIC: ").strip()
            nationality = input("Enter Nationality: ").strip()
            academic_no = input("Enter Academic Number: ").strip()
            service.add_student(first_name, last_name, address, nic, nationality, academic_no)

        elif choice == "2":
            academic_no = input("Enter Academic Number: ").strip()
            student = service.search_student(academic_no)
            print(student.__dict__ if student else "Not found!")

        elif choice == "3":
            academic_no = input("Enter Academic Number to delete: ").strip()
            service.delete_student(academic_no)

        elif choice == "4":
            academic_no = input("Enter Academic Number: ").strip()
            address = input("Enter new Address: ").strip()
            service.update_contact(academic_no, address)

        elif choice == "5":
            for student in service.view_all_students():
                print(student.__dict__)

        elif choice == "6":
            academic_no = input("Enter Academic Number: ").strip()
            subject = input("Enter Subject: ").strip()
            mark = float(input("Enter Mark: "))
            service.add_subject_marks(academic_no, subject, mark)

        elif choice == "7":
            academic_no = input("Enter Academic Number: ").strip()
            marks = service.view_student_marks(academic_no)
            print(marks if marks else "No marks found.")

        elif choice == "8":
            academic_no = input("Enter Academic Number: ").strip()
            avg = service.show_average_marks(academic_no)
            print(f"Average Marks: {avg}" if avg is not None else "No marks found.")

        elif choice == "9":
            print("Exiting...")
            break

        else:
            print("Invalid choice.. Try again!")

if __name__ == "__main__":
    main()
