from .schedule_management import ScheduleManagment
from .schedule_management_visitor import ScheduleManagementVisitor


class RemoteWorkShiftScheduleManagment(ScheduleManagment):
    def generate_report(self) -> None:
        print("Generating remote work shift report...")

    def calculating_overtime(self) -> None:
        print("Calculating remote work shift overtime...")

    def accept(self, visitor: ScheduleManagementVisitor) -> None:
        visitor.visit_remote_work_shift(self)
