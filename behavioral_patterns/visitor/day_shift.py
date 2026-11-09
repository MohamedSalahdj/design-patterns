from .schedule_management import ScheduleManagment


class DayShiftScheduleManagment(ScheduleManagment):
    def generate_report(self) -> None:
        print("Generating day shift report...")

    def calculating_overtime(self) -> None:
        print("Calculating day shift overtime...")

    def manage_leave_report(self) -> None:
        print("Managing day shift leave report...")
