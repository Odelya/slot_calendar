from abc import ABC, abstractmethod

class CalendarInputParser(ABC):

    @abstractmethod
    def parse(self):
        pass