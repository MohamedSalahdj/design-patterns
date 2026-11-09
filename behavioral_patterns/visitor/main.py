from .schedule_management import ScheduleManagment
from .day_shift import DayShiftScheduleManagment
from .night_shift import NightShiftScheduleManagment
from .remote_work_shift import RemoteWorkShiftScheduleManagment
from .management_leave_request_visitor import ManagementLeaveRequestVisitor
from .calculate_bonus_visitor import CalculateBonusVisitor

if __name__ == "__main__":
    shifts: list[ScheduleManagment] = [
        DayShiftScheduleManagment(),
        NightShiftScheduleManagment(),
        RemoteWorkShiftScheduleManagment(),
    ]

    for shift in shifts:
        shift.generate_report()
        shift.calculating_overtime()
        shift.accept(ManagementLeaveRequestVisitor())
        shift.accept(CalculateBonusVisitor())
        print("-" * 30)
