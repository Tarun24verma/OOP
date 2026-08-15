def attendance_percentage(attendance:int,total_work_days:int)->tuple[int,bool]:
    attendance = (attendance/total_work_days)*100
    return f"{attendance}, Eligibility: {attendance>=75}"