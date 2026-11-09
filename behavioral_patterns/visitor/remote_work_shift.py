from .schedule_management import ScheduleManagment


class RemoteWorkShiftScheduleManagment(ScheduleManagment):
    def generate_report(self) -> None:
        print("Generating remote work shift report...")

    def calculating_overtime(self) -> None:
        print("Calculating remote work shift overtime...")

    def manage_leave_report(self) -> None:
        print("Managing remote work shift leave report...")
