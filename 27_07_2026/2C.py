def calculate_average(Marks:list[int])->float:
    if Marks:
        return sum(Marks)/len(Marks)
    return 0.0
def display_student(name:str, *marks:int, **info)->None:
    print(f"Name: {name}\nMarks: {tuple(marks)}\nAdditional Info: {info}")
print(calculate_average([70,80,90]))
print(calculate_average([]))
display_student('Aman',85,90,78, section="B", city='Pune')
print(calculate_average.__annotations__)
print(display_student.__annotations__)