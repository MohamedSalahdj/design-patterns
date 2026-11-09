from abc import ABC, abstractmethod


class ScheduleManagementVisitor(ABC):
    @abstractmethod
    def visit_day_shift(self, day_shift: "DayShiftScheduleManagment") -> None:
        ...

    @abstractmethod
    def visit_night_shift(self, night_shift: "NightShiftScheduleManagment") -> None:
        ...

    @abstractmethod
    def visit_remote_work_shift(
        self, remote_work_shift: "RemoteWorkShiftScheduleManagment"
    ) -> None:
        ...
