def attendance_percentage(attendance:int,total_work_days:int)->tuple[int,bool]:
    attendance = (attendance/total_work_days)*100
    return attendance, attendance>=75