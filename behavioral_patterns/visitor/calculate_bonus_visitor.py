from .schedule_management_visitor import ScheduleManagementVisitor


class CalculateBonusVisitor(ScheduleManagementVisitor):
    def visit_day_shift(self, day_shift: "DayShiftScheduleManagment") -> None:
        print("Calculating bonus for day shift...")

    def visit_night_shift(self, night_shift: "NightShiftScheduleManagment") -> None:
        print("Calculating bonus for night shift...")

    def visit_remote_work_shift(
        self, remote_work_shift: "RemoteWorkShiftScheduleManagment"
    ) -> None:
        print("Calculating bonus for remote work shift...")
