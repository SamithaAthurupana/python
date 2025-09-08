# Importing Abstract Base Class (ABC) and abstractmethod decorator
# Used to define abstract classes (interfaces) that must be implemented
from abc import ABC, abstractmethod  

# Typing imports for type hints
from typing import List, Dict  

# Importing models (Book, Member, Loan) which are assumed to be dataclasses or normal classes
from models import Book, Member, Loan  


# -------------------- ABSTRACT REPOSITORIES --------------------

# Abstract repository for Book entities
class BookRepository(ABC):

    @abstractmethod
    def add(self, book: Book) -> None:  
        # Add a new book to storage (abstract method, must be implemented in subclass)
        pass  

    @abstractmethod
    def get_book_by_id(self, book_id: str) -> Book:  
        # Fetch a book by its ID
        pass  

    @abstractmethod
    def update(self, book: Book):  
        # Update book details
        pass  

    @abstractmethod
    def list_all_books(self) -> List[Book]:  
        # Return all books as a list
        pass  


# Abstract repository for Member entities
class MemberRepository(ABC):

    @abstractmethod
    def add(self, member: Member) -> None:  
        # Add a new member
        pass  

    @abstractmethod
    def get_member_by_id(self, member_id: str) -> Member:  
        # Fetch a member by their ID
        pass  

    @abstractmethod
    def list_all_members(self) -> List[Member]:  
        # Return all members
        pass  


# Abstract repository for Loan entities
class LoanRepository(ABC):

    @abstractmethod
    def add(self, loan: Loan) -> None:  
        # Add a new loan
        pass  

    @abstractmethod
    def get_by_id(self, loan_id: str) -> Loan:  
        # Fetch loan by its ID
        pass  

    @abstractmethod
    def update(self, loan: Loan) -> None:  
        # Update loan details
        pass  

    @abstractmethod
    def list_all_loans(self) -> List[Loan]:  
        # Return all loans
        pass  


# -------------------- IN-MEMORY IMPLEMENTATIONS --------------------

# In-memory storage implementation of BookRepository
class InMemoryBookRepository(BookRepository):
    def __init__(self):
        # Private dictionary to store books (book_id -> Book object)
        self.__book: Dict[str, Book] = {}

    def add(self, book: Book) -> None:
        # Add or overwrite book by ID
        self.__book[book.book_id] = book

    def get_book_by_id(self, book_id: str) -> Book:
        # Return book by ID, or None if not found
        return self.__book.get(book_id)

    def update(self, book: Book) -> None:
        # Update existing book (overwrites if exists)
        self.__book[book.book_id] = book

    def list_all_books(self) -> List[Book]:
        # Return list of all stored Book objects
        return list(self.__book.values())


# In-memory storage implementation of MemberRepository
class InMemoryMemberRepository(MemberRepository):

    def __init__(self):
        # Private dictionary for members (member_id -> Member object)
        self.__members: Dict[str, Member] = {}

    def add(self, member: Member) -> None:
        # Add or overwrite member
        self.__members[member.member_id] = member

    def get_member_by_id(self, member_id: str) -> Member:
        # Return member by ID, or None if not found
        return self.__members.get(member_id)

    def list_all_members(self) -> List[Member]:
        # Return list of all Member objects
        return list(self.__members.values())


# In-memory storage implementation of LoanRepository
class InMemoryMemberLoanRepository(LoanRepository):

    def __init__(self):
        # Private dictionary for loans (loan_id -> Loan object)
        self.__loans: Dict[str, Loan] = {}

    def add(self, loan: Loan) -> None:
        # Add or overwrite loan
        self.__loans[loan.loan_id] = loan

    def get_by_id(self, loan_id: str) -> Loan:
        # Return loan by ID, or None if not found
        return self.__loans.get(loan_id)

    def update(self, loan: Loan) -> None:
        # Update existing loan (overwrites if exists)
        self.__loans[loan.loan_id] = loan

    def list_all_loans(self) -> List[Loan]:
        # Return list of all Loan objects
        return list(self.__loans.values())


# -------------------- DATABASE IMPLEMENTATION (STUB) --------------------

# Placeholder for a database-backed repository for books
class InDatabaseRepository(BookRepository):
    def add(self, book: Book) -> None:
        # TODO: Implement database insert
        pass  

    def get_book_by_id(self, book_id: str) -> Book:
        # TODO: Implement database fetch
        pass  

    def update(self, book: Book):
        # TODO: Implement database update
        pass  

    def list_all_books(self) -> List[Book]:
        # TODO: Implement fetch all from database
        pass  
