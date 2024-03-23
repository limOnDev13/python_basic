from abc import ABC
from typing import Optional


class Date(ABC):
    def __init__(self):
        self.__day: Optional[int] = None
        self.__month: Optional[int] = None
        self.__year: Optional[int] = None

    @classmethod
    def from_string(cls, date_string: str) -> 'Date':
        return self


date: Date = Date.from_string('123', '12321')
