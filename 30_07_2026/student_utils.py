def ave(nums:list)->int:
    """This Function calculates the average."""
    return sum(nums)/len(nums)

def pass_status(average:int, passing_marks=40)->bool:
    """This function checks whether the student passed or not"""
    return average>=passing_marks

def grade(average:int)->str:
    """this function alots grades"""
    if average>90:return 'O'
    elif average>=50:return 'A'
    else: return 'F'
