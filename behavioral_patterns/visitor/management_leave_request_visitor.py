from .schedule_management_visitor import ScheduleManagmentVisitor


class ManagementLeaveRequestVisitor(ScheduleManagmentVisitor):
    def visit_day_shift(self, day_shift: "DayShiftScheduleManagment") -> None:
        print("Managing leave request for day shift...")

    def visit_night_shift(self, night_shift: "NightShiftScheduleManagment") -> None:
        print("Managing leave request for night shift...")

    def visit_remote_work_shift(
        self, remote_work_shift: "RemoteWorkShiftScheduleManagment"
    ) -> None:
        print("Managing leave request for remote work shift...")