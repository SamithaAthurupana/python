from datetime import datetime
from dataclasses import dataclass
from models import Book, Member, Loan
from repositories import BookRepository, LoanRepository, MemberRepository

class LibraryError(Exception):
    pass

@dataclass
class LibraryService:
    books: BookRepository
    members: MemberRepository
    loans: LoanRepository
    # def __init__(self, books: BookRepository, members: MemberRepository, loans: LoanRepository):
    #     self.books = books
    #     self.members = members
    #     self.loans = loans

    def add_book(self, book_id:str, title:str, author:str, year:str) -> Book:
        if self.books.get_book_by_id(book_id) is not None:
            raise LibraryError(f"Book already Exists with book id - {book_id}")

        book = Book(book_id=book_id, title=title, author=author, year=year) # creating a book object
        self.books.add(book)
        return book

    def register_member(self,member_id:str, name:str) -> Member:
        if self.members.get_member_by_id(member_id) is not None:
            raise LibraryError(f"Member already Exists with member id - {member_id}")

        member = Member(member_id=member_id, name=name)
        self.members.add(member)
        return member

    def list_all_books(self):
        return self.books.list_all_books()

    def borrow_book(self, loan_id:str, book_id:str, member_id:str) -> Loan:
        if self.books.get_book_by_id(book_id) is None:
            raise LibraryError("Book not found")

        if self.members.get_member_by_id(member_id) is None:
            raise LibraryError("Member not found")

        if not self.books.get_book_by_id(book_id).is_available():
            raise LibraryError("Book Not Available")

        loan = Loan(loan_id, member_id, book_id, datetime.now())
        book = self.books.get_book_by_id(book_id)
        book.book_lend_member_id = member_id
        self.books.update(book)
        self.loans.add(loan)
        return loan

    def return_book(self, loan_id:str) -> Loan:
        loan = self.loans.get_by_id(loan_id)

        if loan is None:
            raise LibraryError("loan doesn't exist")

        if loan.is_active():
            raise LibraryError("Loan is not active")

        book = self.books.get_book_by_id(loan.book_id)
        book.book_lend_member_id = None
        self.books.update(book)

        loan.returned_at = datetime.now()
        self.loans.update(loan)
        return loan

    def list_all_loans(self):
        return [loan for loan in self.loans.list_all_loans() if loan.is_active()]


