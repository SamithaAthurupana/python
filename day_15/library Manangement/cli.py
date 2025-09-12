import time

from service import LibraryService, LibraryError
from repositories import InMemoryMemberRepository, InMemoryMemberLoanRepository, InMemoryBookRepository

library_service = LibraryService(
    books=InMemoryBookRepository(),
    loans=InMemoryMemberLoanRepository(),
    members=InMemoryMemberRepository()
)

def list_book():
    books = library_service.list_all_books()
    if not books:
        print("No books available in library.")
    else:
        for book in books:
            status = "Available" if book.is_available() else f"Out by - {book.book_lend_member_id}"
            print(f"Book id - {book.book_id} | Title - {book.title} | "
                  f"Author - {book.author} | Year - {book.year} | Status - {status}")
    time.sleep(2)

def add_book():
    book_id = input("Enter book id: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter book year: ")
    try:
        library_service.add_book(book_id, title, author, year)
        print("Book added successfully!")
    except LibraryError as e:
        print(e)
    time.sleep(2)

def add_member():
    member_id = input("Enter member id: ")
    name = input("Enter member name: ")
    try:
        library_service.register_member(member_id, name)
        print("Member registered successfully!")
    except LibraryError as e:
        print(e)
    time.sleep(2)

def borrow_book():
    loan_id = input("Enter loan id: ")
    book_id = input("Enter book id: ")
    member_id = input("Enter member id: ")
    try:
        loan = library_service.borrow_book(loan_id, book_id, member_id)
        print(f"Book {loan.book_id} borrowed successfully by member {loan.member_id}!")
    except LibraryError as e:
        print(e)
    time.sleep(2)

def return_book():
    loan_id = input("Enter loan id: ")
    try:
        loan = library_service.return_book(loan_id)
        print(f"Book {loan.book_id} returned successfully!")
    except LibraryError as e:
        print(e)
    time.sleep(2)


while True:
    print("""
    ********************************************
    -------- LIBRARY MANAGEMENT SYSTEM ---------
    1.) PRESS 1 TO LIST BOOKS
    2.) PRESS 2 TO ADD BOOKS
    3.) PRESS 3 TO ADD MEMBER
    4.) PRESS 4 TO BORROW BOOKS
    5.) PRESS 5 TO RETURN BOOK
    6.) PRESS 6 TO EXIT
    ********************************************
    """)
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Enter a number.\n")
        continue

    if choice == 1:
        list_book()
    elif choice == 2:
        add_book()
    elif choice == 3:
        add_member()
    elif choice == 4:
        borrow_book()
    elif choice == 5:
        return_book()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
