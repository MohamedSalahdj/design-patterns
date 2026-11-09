from abc import ABC, abstractmethod
from .schedule_management_visitor import ScheduleManagmentVisitor


class ScheduleManagment(ABC):
    @abstractmethod
    def generate_report(self) -> None:
        ...

    @abstractmethod
    def calculating_overtime(self) -> None:
        ...

    @abstractmethod
    def accept(self, visitor: ScheduleManagmentVisitor) -> None:
        ...
