#objects & blue prints
import datetime
from dataclasses import dataclass
from typing import List, Optional, Dict


@dataclass  # dataclass කියන්නේ class එකක් define කරනකොට boilerplate code (constructor, repr, equality methods වගේ) auto-generate කරන decorator එක.
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

