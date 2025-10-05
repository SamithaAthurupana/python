import datetime  # Used to calculate birthdays and ages from NIC

student_information = {}  # Dictionary to hold all student data
auto_increment = 1  # Counter used for generating unique Student IDs

def generate_student_id(nic):
    """
    Generate a unique student ID using:
    - Last 4 digits of NIC
    - Auto increment number (formatted as 001, 002, etc.)
    Example: NIC = 200012345678 → Student ID = 5678-001
    """
    global auto_increment
    student_id = f"{nic[-4:]}-{auto_increment:03d}"  # Use last 4 NIC digits + formatted counter
    auto_increment += 1  # Increase counter for next student
    return student_id


def get_birthday_from_nic(nic):
    """
    Extract birthday from NIC.
    NIC formats:
      - Old (10 digits): YYDDDxxxxV
      - New (12 digits): YYYYDDDxxxxx
    Rules:
      - DDD = Day of year (1–366). If > 500 → Female, so subtract 500 to get real day.
    """
    try:
        if len(nic) == 10:  # Old NIC
            year = 1900 + int(nic[:2])  # First 2 digits → Year (assume 1900s)
            day_of_year = int(nic[2:5])  # Next 3 digits → Day of year
        elif len(nic) == 12:  # New NIC
            year = int(nic[:4])  # First 4 digits → Year
            day_of_year = int(nic[4:7])  # Next 3 digits → Day of year
        else:
            return None  # Invalid NIC

        # Adjust for gender (if > 500 → Female → subtract 500 to get actual day)
        if day_of_year > 500:
            day_of_year -= 500

        # Convert "day of year" → actual date
        date = datetime.datetime(year, 1, 1) + datetime.timedelta(days=day_of_year - 1)
        return date.date()  # Return as YYYY-MM-DD
    except:
        return None  # If NIC invalid → return None


def get_age_from_nic(nic):
    """
    Calculate current age using birthday extracted from NIC.
    Formula:
      Today_Year - Birth_Year
      (adjust if birthday hasn’t occurred yet this year)
    """
    birthday = get_birthday_from_nic(nic)  # Get date of birth
    if not birthday:
        return None
    today = datetime.date.today()  # Get today’s date
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age


def get_gender_from_nic(nic):
    """
    Determine gender from NIC.
    Rule:
      Day of year > 500 → Female
      Day of year <= 500 → Male
    """
    try:
        if len(nic) == 10:
            day_of_year = int(nic[2:5])
        elif len(nic) == 12:
            day_of_year = int(nic[4:7])
        else:
            return "Unknown"  # Invalid NIC

        return "Female" if day_of_year > 500 else "Male"
    except:
        return "Unknown"


def add_student(students, first_name, last_name, address, nic, nationality, academic_no):
    student_id = generate_student_id(nic)  # Auto-generate Student ID
    birthday = get_birthday_from_nic(nic)  # Extract birthday
    age = get_age_from_nic(nic)  # Calculate age
    gender = get_gender_from_nic(nic)  # Find gender

    # Store all details in dictionary
    students[student_id] = {
        "first_name": first_name,
        "last_name": last_name,
        "address": address,
        "nic": nic,
        "nationality": nationality,
        "academic_no": academic_no,
        "birthday": str(birthday),
        "age": age,
        "gender": gender
    }
    print(f"Student {first_name} {last_name} added with ID {student_id}.")


def search(students, student_id):
    """Search and display student details by ID."""
    if student_id in students:
        print(f"Student ID: {student_id} -> {students[student_id]}")
    else:
        print("Student not found.")


def delete_student(students, student_id):
    """Delete student by ID."""
    if student_id in students:
        del students[student_id]
        print(f"Student ID {student_id} deleted successfully.")
    else:
        print("Student not found!")


def update_student_contact(students, student_id, updated_no):
    """Update student’s contact number (only if student exists)."""
    if student_id in students:
        students[student_id]["contact"] = updated_no  # Add contact field dynamically
        print(f"Contact updated for {students[student_id]['first_name']}.")
    else:
        print("Student not found.")


def view_student_names(students):
    """Show all student IDs and names in system."""
    if not students:
        print("No student records available.")
    else:
        for student_id, details in students.items():
            print(f"ID: {student_id} | Name: {details['first_name']} {details['last_name']}")


def add_student_marks(students, student_id):
    """Add subject marks for a student."""
    if student_id in students:
        # Ask marks for 3 subjects
        maths = int(input("Enter marks for Maths: "))
        science = int(input("Enter marks for Science: "))
        history = int(input("Enter marks for History: "))

        # Save marks in nested dictionary
        students[student_id]["marks"] = {
            "maths": maths,
            "science": science,
            "history": history
        }
        print("Marks added successfully.")
    else:
        print("Student not found.")


def view_student_marks(students, student_id):
    """View marks of a student."""
    if student_id in students:
        if "marks" in students[student_id]:  # Check if marks available
            print(f"Marks for {students[student_id]['first_name']} {students[student_id]['last_name']}:")
            for subject, marks in students[student_id]["marks"].items():
                print(f"   {subject.capitalize()}: {marks}")
        else:
            print("Marks not available.")
    else:
        print("Student not found.")


def show_student_averages(students):
    """Show average marks for each student."""
    if not students:
        print("No student records available.")
        return

    for student_id, student_data in students.items():
        if "marks" in student_data:  # Only if marks exist
            total = sum(student_data["marks"].values())  # Sum all subjects
            average = total / len(student_data["marks"])  # Average = total ÷ no. of subjects
            print(f"{student_data['first_name']} {student_data['last_name']} - Average: {average:.2f}")
        else:
            print(f"{student_data['first_name']} {student_data['last_name']} - No marks available.")


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
    ====================================
    """)


def main():
    while True:
        show_menu()  # Show menu each time
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            # Take only required inputs from user
            first_name = input("Enter First Name: ").strip()
            last_name = input("Enter Last Name: ").strip()
            address = input("Enter Address: ").strip()
            nic = input("Enter NIC: ").strip()
            nationality = input("Enter Nationality: ").strip()
            academic_no = input("Enter Academic Number: ").strip()

            add_student(student_information, first_name, last_name, address, nic, nationality, academic_no)

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
            print("👋 Exiting program. Goodbye!")
            break  # Exit the loop → Program ends

        else:
            print("Invalid choice. Please enter 1-9.")


main()  # Start the system
