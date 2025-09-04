import time

from service import LibraryService, LibraryError
from repositories import InMemoryMemberRepository, InMemoryMemberLoanRepository, InMemoryBookRepository

library_service = LibraryService(books=InMemoryBookRepository(),
                                 loans=InMemoryMemberLoanRepository(),
                                 members= InMemoryMemberRepository())
def list_book():
    books = library_service.list_all_books()

    for book in books:
        status = "Available" if book.is_available() else f"Out by - {book.book_lend_member_id}"
        print(f"Book id - {book.book_id} Title - {book.title} "
              f"Author - {book.author} year - {book.year} status - {status}")
    time.sleep(10)
def add_book():

    book_id = input("Enter book id: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter book year: ")
    try:
        library_service.add_book(book_id,title,author,year)
    except LibraryError as e:
        print(e)



while True:
    print("""
    ********************************************
    -------- LIBRARY MANAGEMENT SYSTEM ---------
    1.) PRESS 1 TO LIST BOOKS
    2.) PRESS 2 TO ADD BOOKS
    3.) PRESS 3 TO ADD MEMBER
    4.) PRESS 4 TO BORROW BOOKS
    5.) PRESS 5 TO RETURN BOOK
    ********************************************
    """)
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Enter a number.\n")
        continue

    if choice == 1:
        list_book()

    if choice == 2:
        add_book()