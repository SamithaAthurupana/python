from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Student:
    first_name: str
    last_name: str
    address: str
    nic: str
    nationality: str
    academic_year: str
    contacts: List[Dict[str, str]] = None  # list of dictionaries for contacts

    def __post_init__(self):
        if self.contacts is None:
            self.contacts = []

    def add_contact(self) -> None:
        # get user inputs for one student
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        address = input("Enter address: ")
        nic = input("Enter NIC: ")
        nationality = input("Enter nationality: ")
        academic_year = input("Enter academic year: ")

        contact = {
            "First Name": first_name,
            "Last Name": last_name,
            "Address": address,
            "NIC": nic,
            "Nationality": nationality,
            "Academic Year": academic_year
        }
        self.contacts.append(contact)
        print(f"\nStudent added: {contact}\n")

    def show_info(self) -> None:
        if not self.contacts:
            print("No students available.")
        else:
            print("\nAll Students:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact}")


# Main Program
student_manager = Student(
    first_name="", last_name="", address="", nic="", nationality="", academic_year=""
)

print("************* Student Management System *******************\n")

while True:
    print("""
    ********************************************
    1.) ADD A NEW STUDENT
    2.) SHOW ALL STUDENTS
    3.) EXIT
    ********************************************
    """)
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Enter a number.\n")
        continue

    if choice == 1:
        student_manager.add_contact()
    elif choice == 2:
        student_manager.show_info()
    elif choice == 3:
        print("Exiting system...")
        break
    else:
        print("Invalid choice. Try again.\n")
