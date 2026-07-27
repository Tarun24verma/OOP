"""Practical 2C — Type Hints and Function Annotations
Write a function named `calculate_average()` that:
Accepts a list of integers
Returns a floating-point average
Uses type hints for the parameter and return value
Returns `0.0` when the list is empty
Write a second function named `display_student()` that:
Accepts `name` as a string
Accepts `marks` using `*args` with integer type hints
Accepts additional student information using `**kwargs`
Returns `None`
Displays the name, marks, and additional information
Call both functions, then print the `__annotations__` attribute of both functions.
Expected Sample Output:
```
80.0
0.0
Name: Aman
Marks: (85, 90, 78)
Additional Info: {'section': 'B', 'city': 'Pune'}
{'marks': list[int], 'return': <class 'float'>}
{'name': <class 'str'>, 'marks': <class 'int'>, 'return': None}
```"""


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