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
        self.__book: Dict[str, Book] = {}   # Private dictionary to store books (book_id -> Book object)

    def add(self, book: Book) -> None:
        self.__book[book.book_id] = book    # Add or overwrite book by ID

    def get_book_by_id(self, book_id: str) -> Book:
        return self.__book.get(book_id)     # Return book by ID, or None if not found

    def update(self, book: Book) -> None:
        self.__book[book.book_id] = book    # Update existing book (overwrites if exists)

    def list_all_books(self) -> List[Book]:
        return list(self.__book.values())   # Return list of all stored Book objects


# In-memory storage implementation of MemberRepository
class InMemoryMemberRepository(MemberRepository):

    def __init__(self):
        self.__members: Dict[str, Member] = {}      # Private dictionary for members (member_id -> Member object)

    def add(self, member: Member) -> None:
        self.__members[member.member_id] = member   # Add or overwrite member

    def get_member_by_id(self, member_id: str) -> Member:
        return self.__members.get(member_id)    # Return member by ID, or None if not found

    def list_all_members(self) -> List[Member]:
        return list(self.__members.values())    # Return list of all Member objects


# In-memory storage implementation of LoanRepository
class InMemoryMemberLoanRepository(LoanRepository):

    def __init__(self):
        self.__loans: Dict[str, Loan] = {}      # Private dictionary for loans (loan_id -> Loan object)

    def add(self, loan: Loan) -> None:
        self.__loans[loan.loan_id] = loan   # Add or overwrite loan

    def get_by_id(self, loan_id: str) -> Loan:
        return self.__loans.get(loan_id)    # Return loan by ID, or None if not found

    def update(self, loan: Loan) -> None:
        self.__loans[loan.loan_id] = loan   # Update existing loan (overwrites if exists)

    def list_all_loans(self) -> List[Loan]:
        return list(self.__loans.values())  # Return list of all Loan objects


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
