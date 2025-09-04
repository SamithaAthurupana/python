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

    def extract_nic_info(self, nic: str) -> Dict[str, str]:
        """Extract gender and birth year from NIC"""
        year, gender = "Unknown", "Unknown"

        if len(nic) == 10 and nic[-1].isalpha():  # Old NIC
            year_prefix = "19"  # Old NIC only for 1900s
            year = int(year_prefix + nic[:2])
            day_text = int(nic[2:5])
        elif len(nic) == 12:  # New NIC
            year = int(nic[:4])
            day_text = int(nic[4:7])
        else:
            return {"Year": year, "Gender": gender}

        # Determine gender
        if day_text > 500:
            gender = "Female"
            day_text -= 500
        else:
            gender = "Male"

        return {"Year": str(year), "Gender": gender}

    def add_contact(self) -> None:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        address = input("Enter address: ")
        nic = input("Enter NIC: ")
        nationality = input("Enter nationality: ")
        academic_year = input("Enter academic year: ")

        nic_info = self.extract_nic_info(nic)

        contact = {
            "First Name": first_name,
            "Last Name": last_name,
            "Address": address,
            "NIC": nic,
            "Nationality": nationality,
            "Academic Year": academic_year,
            "Birth Year": nic_info["Year"],
            "Gender": nic_info["Gender"]
        }
        self.contacts.append(contact)
        print(f"\n✅ Student added successfully!\n")

    def show_info(self) -> None:
        if not self.contacts:
            print("No students available.")
        else:
            print("\n📋 All Students:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact}")

    def search_by_nic(self, nic: str) -> None:
        found = False
        for contact in self.contacts:
            if contact["NIC"] == nic:
                print("\n🔎 Student Found:")
                print(contact)
                found = True
                break
        if not found:
            print("❌ No student found with this NIC.")

    def delete_student(self, nic: str) -> None:
        for contact in self.contacts:
            if contact["NIC"] == nic:
                self.contacts.remove(contact)
                print("🗑️ Student deleted successfully.")
                return
        print("❌ No student found with this NIC.")


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
    3.) SEARCH STUDENT BY NIC
    4.) DELETE STUDENT BY NIC
    5.) EXIT
    ********************************************
    """)
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("⚠️ Invalid input. Enter a number.\n")
        continue

    if choice == 1:
        student_manager.add_contact()
    elif choice == 2:
        student_manager.show_info()
    elif choice == 3:
        nic = input("Enter NIC to search: ")
        student_manager.search_by_nic(nic)
    elif choice == 4:
        nic = input("Enter NIC to delete: ")
        student_manager.delete_student(nic)
    elif choice == 5:
        print("👋 Exiting system...")
        break
    else:
        print("⚠️ Invalid choice. Try again.\n")
