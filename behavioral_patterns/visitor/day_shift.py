from .schedule_management import ScheduleManagment
from .schedule_management_visitor import ScheduleManagementVisitor


class DayShiftScheduleManagment(ScheduleManagment):
    def generate_report(self) -> None:
        print("Generating day shift report...")

    def calculating_overtime(self) -> None:
        print("Calculating day shift overtime...")

    def accept(self, visitor: ScheduleManagementVisitor) -> None:
        visitor.visit_day_shift(self)
