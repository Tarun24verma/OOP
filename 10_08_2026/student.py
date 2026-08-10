class Student:
    School='Gayhearts'
    def __init__(self, name, roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display(self):
        print(f'Name: {self.name}\nSchool:{self.School}\nRoll No.: {self.roll}\nMarks: {self.marks}')
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        return "Fail"


class BankAccount:
    interest_rate=0.02
    def __init__(self, balance):
        self.balance=balance
    def apply(self):
        return (self.balance*self.interest_rate)+self.balance
