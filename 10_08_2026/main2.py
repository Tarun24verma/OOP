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

if __name__=="__main__":
    student1=Student("Alice", 1, 95)
    student1.display()
    print(f"Grade: {student1.grade()}")

    student2=Student("Bob", 2, 80)
    student2.display()
    print(f"Grade: {student2.grade()}")

    student3=Student("Charlie", 3, 50)
    student3.display()
    print(f"Grade: {student3.grade()}")

class BankAccount:
    interest_rate=0.02
    def __init__(self, balance):
        self.balance=balance
    def apply(self):
        return (self.balance*self.interest_rate)+self.balance
if __name__=="__main__":
    account1=BankAccount(1000)
    print(f"New Balance after interest: {account1.apply()}")