#objects & blue prints
import datetime
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Book:
    book_id: str
    title: str
    author: str
    year: str
    book_lend_member_id : Optional[str] = None

@dataclass
class Member:
    member_id: str
    name: str

@dataclass
class Loan:
    loan_id: str
    member_id: str
    book_id: str
    borrow_at: datetime
    returned_at: Optional[datetime] = None