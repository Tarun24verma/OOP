"""Practical 1B — Variable-Length Arguments
Write a function named `student_report()` that:
Accepts any number of marks using `*args`
Accepts student details such as `name`, `roll_no`, and `section` using `**kwargs`
Displays the student details
Calculates total marks
Calculates average marks
Displays the highest and lowest marks
Sample call:
```
student_report(85, 90, 78, 92, name="Riya", roll_no=21, section="A")
```
Expected Sample Output:
```
Name: Riya
Roll No: 21
Section: A
Total Marks: 345
Average Marks: 86.25
Highest Marks: 92
Lowest Marks: 78
```"""


def student_report(*marks,**kwargs): 
    for x,y in kwargs.items():
        label = x.replace("_", " ").title()
        print(f"{label}: {y}")
    avg=sum(marks)/len(marks)
    print(f"Total Marks: {sum(marks)}")
    print(f"Average Marks: {avg}")
    print(f"Highest Marks: {max(marks)}")
    print(f"Lowest Marks: {min(marks)}")
student_report(85, 90, 78, 92, name="Riya", roll_no=21, section="A")