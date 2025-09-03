from abc import ABC, abstractmethod
from typing import List, Dict
from models import Book, Member, Loan

class BookRepository(ABC):

    @abstractmethod
    def add(self, book: Book) -> None:
        pass

    @abstractmethod
    def get_book_by_id(self, book_id:str) -> Book:
        pass

    @abstractmethod
    def update(self, book: Book):
        pass

    @abstractmethod
    def list_all_books(self) -> List[Book]:
        pass

class MemberRepository(ABC):

    @abstractmethod
    def add(self, member: Member) -> None:
        pass

    @abstractmethod
    def get_member_by_id(self, member_id:str) -> Member:
        pass

    @abstractmethod
    def list_all_members(self) -> List[Member]:
        pass


class LoanRepository(ABC):

    @abstractmethod
    def add(self, loan: Loan) -> None:
        pass

    @abstractmethod
    def get_by_id(self, loan_id: str) -> Loan:
        pass

    @abstractmethod
    def update(self, loan:Loan) -> None:
        pass

    @abstractmethod
    def list_all_loans(self) -> List[Loan]:
        pass

class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.__book: Dict[str, Book] = {}

    def add(self, book: Book) -> None:
        self.__book[book.book_id] = book

    def get_book_by_id(self, book_id: str) -> Book:
        return self.__book.get(book_id)

    def update(self, book: Book) -> None:
        self.__book[book.book_id] = book

    def list_all_books(self) -> List[Book]:
        return list(self.__book.values())

class InMemoryMemberRepository(MemberRepository):

    def __init__(self):
        self.__members: Dict[str, Member] = {}

    def add(self, member:Member) -> None:
        self.__members[member.member_id] = member

    def get_member_by_id(self, member_id: str) -> Member:
        return self.__members.get(member_id)

    def list_all_members(self) -> List[Member]:
        return list(self.__members.values())

class InMemoryMemberLoanRepository(LoanRepository):

    def __init__(self):
        self.__loans:Dict[str, Loan] = {}

    def add(self, loan: Loan) -> None:
        self.__loans[loan.loan_id] = loan

    def get_by_id(self, loan_id: str) -> Loan:
        return self.__loans.get(loan_id)

    def update(self, loan: Loan) -> None:
        self.__loans[loan.loan_id] = loan

    def list_all_loans(self) -> List[Loan]:
        return list(self.__loans.values())