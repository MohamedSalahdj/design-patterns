from abc import ABC, abstractmethod


class ScheduleManagment(ABC):
    @abstractmethod
    def generate_report(self) -> None:
        ...

    @abstractmethod
    def calculating_overtime(self) -> None:
        ...

    @abstractmethod
    def manage_leave_report(self) -> None:
        ...
