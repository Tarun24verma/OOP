class Employee:
    ALLOWANCE_RATE = 0.2
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary
        if base_salary <= 0:
            print(f"Invalid salary entered for {name}. Salary set to 0.")
            base_salary = 0
        self.base_salary = base_salary
    def calculate_salary(self):
        return self.base_salary + (self.base_salary*self.ALLOWANCE_RATE)
    def display(self):
        print(f"Employee ID : {self.emp_id}")
        print(f"Name        : {self.name}")
        print(f"Salary      : Rs.{self.calculate_salary():.2f}")
class Manager(Employee):
    BONUS_PER_MEMBER = 2000
    def __init__(self, emp_id, name, base_salary, team_size):
        super().__init__(emp_id, name, base_salary)
        self.team_size = team_size
    def calculate_salary(self):
        return super().calculate_salary() + (self.team_size * self.BONUS_PER_MEMBER)
    def display(self):
        super().display()
        print(f"Role        : Manager(Team Size {self.team_size})")
class Director(Manager):
    def __init__(self, emp_id, name, base_salary, team_size, director_bonus):
        super().__init__(emp_id, name, base_salary, team_size)
        self.director_bonus = director_bonus
    def calculate_salary(self):
        return super().calculate_salary() + self.director_bonus
    def display(self):
        super().display()
        print(f"Role        : Director (Bonus Rs.{self.director_bonus})")

Employee1=Employee("E101", "Asha", 30000)
manager1=Manager("M201", "Ravi", 50000, 5)
director1=Director("D301", "Meena", 90000, 10, 50000)
l=[Employee1, manager1, director1]
total_pay=0
for emp in l:
    emp.display()
    total_pay += emp.calculate_salary()
    print(" ")
print(f"Total Salary Pay: {total_pay}\n")
print(f"MRO of Director: {str(Director.__mro__).replace("<class '__main__.","").replace("'>",' -> ').replace('(',"").replace(")","").replace(" ,", "").replace("<class '", "")[:-3]}\n")
issubclass(Director, Employee)
issubclass(Manager, Employee)
Employee2=Employee("E102", "Raman", -500)