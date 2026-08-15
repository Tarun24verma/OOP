def total_marks(marks:list)->float:
    return sum(marks)

def average_marks(marks:list)->float:
    return sum(marks)/len(marks)

def calculate_grade(average:float)->str:
    if average>90:return 'O'
    elif average>=50:return 'A'
    else: return 'F'

