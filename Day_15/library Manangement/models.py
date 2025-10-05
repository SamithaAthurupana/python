#objects & blue prints
import datetime
from dataclasses import dataclass
from typing import List, Optional

@dataclass  # dataclass කියන්නේ class එකක් define කරනකොට boilerplate code (constructor, repr, equality methods වගේ) auto-generate කරන decorator එක.
class Book:
    book_id: str
    title: str
    author: str
    year: str
    book_lend_member_id : Optional[str] = None # optional property, not necessary to create an object

    def is_available(self) -> bool:
        return self.book_lend_member_id is None # returning true or false if book lend member id exist

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

    def is_active(self) -> bool:
        return self.returned_at is None