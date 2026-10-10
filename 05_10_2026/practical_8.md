# Practical 8: Inheritance and `super()` in Python

**Course:** Object-Oriented Programming using Python
**Topic:** Single inheritance, multilevel inheritance, and the use of `super()`
**Difficulty:** Medium (basic)
**Time:** 1 lab session

---

## 1. Practical Question

Implement single and multilevel inheritance; demonstrate the use of `super()` to access parent class members.

### Problem statement

A company wants a small program to calculate the monthly salary of its staff. There are three kinds of staff: ordinary **employees**, **managers** and **directors**. A manager is also an employee, and a director is also a manager, so they should share code instead of repeating it.

Write a Python program that models this using inheritance.

---

## 2. Class Design

```
Employee            (base class)
    |
    v
Manager             single inheritance:     Employee -> Manager
    |
    v
Director            multilevel inheritance: Employee -> Manager -> Director
```

### 2.1 `Employee` (base class)

| Item | Requirement |
| --- | --- |
| Attributes | `emp_id`, `name`, `base_salary` |
| Class variable | `ALLOWANCE_RATE = 0.20` (allowance is 20% of base salary) |
| `__init__` | Store the three attributes. If `base_salary` is zero or negative, print a message and set it to `0` |
| `calculate_salary()` | Return `base_salary + allowance` (allowance = `base_salary * ALLOWANCE_RATE`) |
| `display()` | Print the employee id, name and total salary |

### 2.2 `Manager` (child of `Employee`)

| Item | Requirement |
| --- | --- |
| New attribute | `team_size` (number of people managed) |
| New class variable | `BONUS_PER_MEMBER = 2000` |
| `__init__` | Take `emp_id`, `name`, `base_salary`, `team_size`. Use `super().__init__()` to set the first three; store `team_size` yourself |
| `calculate_salary()` | Call `super().calculate_salary()` to get the employee salary, then add `team_size * BONUS_PER_MEMBER` |
| `display()` | Use `super().display()`, then print the role and team size |

### 2.3 `Director` (child of `Manager`)

| Item | Requirement |
| --- | --- |
| New attribute | `director_bonus` (a fixed yearly-style bonus given every month in this exercise) |
| `__init__` | Take `emp_id`, `name`, `base_salary`, `team_size`, `director_bonus`. Use `super().__init__()` to set everything the parent handles; store `director_bonus` yourself |
| `calculate_salary()` | Call `super().calculate_salary()` (the manager salary), then add `director_bonus` |
| `display()` | Use `super().display()`, then print the role and the director bonus |

> **Rule:** In `Manager` and `Director`, you must **not** copy the parent's formulas or assignment lines. Reach them through `super()`.

---

## 3. Main Program Requirements

1. Create **one object of each class**:
   - `Employee("E101", "Asha", 30000)`
   - `Manager("M201", "Ravi", 50000, 5)`
   - `Director("D301", "Meena", 90000, 10, 50000)`
2. Store the three objects in a **list** and use a loop to call `display()` on each.
3. After the loop, print the **total salary payout** of the company (the sum of all three salaries).
4. Print the **Method Resolution Order** of `Director` using `Director.__mro__`.
5. Use `issubclass()` and `isinstance()` to show at least two true and one false relationship (for example `issubclass(Director, Employee)` is `True`, `issubclass(Employee, Manager)` is `False`).
6. Create one `Employee` with a base salary of `-500` and show that your validation catches it.

---

## 4. Expected Output (for the data above)

Your formatting may differ, but the **numbers must match**.

```
Employee ID : E101
Name        : Asha
Salary      : Rs.36,000.00

Employee ID : M201
Name        : Ravi
Salary      : Rs.70,000.00
Role        : Manager (team size 5)

Employee ID : D301
Name        : Meena
Salary      : Rs.178,000.00
Role        : Manager (team size 10)
Role        : Director (bonus Rs.50,000.00)

Total payout: Rs.284,000.00

MRO of Director: Director -> Manager -> Employee -> object

Invalid salary entered for Test. Salary set to 0.
```

### Check your numbers

| Staff | Calculation | Salary |
| --- | --- | --- |
| Asha (Employee) | 30,000 + 20% of 30,000 = 30,000 + 6,000 | 36,000 |
| Ravi (Manager) | (50,000 + 10,000) + 5 x 2,000 = 60,000 + 10,000 | 70,000 |
| Meena (Director) | (90,000 + 18,000) + 10 x 2,000 = 108,000 + 20,000 = 128,000, then + 50,000 | 178,000 |

---

## 5. Instructions

- Write the whole program in a single file named `payroll.py`.
- Use meaningful variable names and add a short comment above each class and method.
- Every constructor in a child class must call `super().__init__()`.
- Do not use any external libraries.
- Run the program and check that your output matches the numbers above.
