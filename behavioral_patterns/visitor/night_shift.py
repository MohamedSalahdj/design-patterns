from .schedule_management import ScheduleManagment


class NightShiftScheduleManagment(ScheduleManagment):
    def generate_report(self) -> None:
        print("Generating night shift report...")

    def calculating_overtime(self) -> None:
        print("Calculating night shift overtime...")

    def manage_leave_report(self) -> None:
        print("Managing night shift leave report...")
