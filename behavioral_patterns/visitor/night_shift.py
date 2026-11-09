from .schedule_management import ScheduleManagment
from .schedule_management_visitor import ScheduleManagmentVisitor


class NightShiftScheduleManagment(ScheduleManagment):
    def generate_report(self) -> None:
        print("Generating night shift report...")

    def calculating_overtime(self) -> None:
        print("Calculating night shift overtime...")

    def accept(self, visitor: ScheduleManagmentVisitor) -> None:
        visitor.visit_night_shift(self)
