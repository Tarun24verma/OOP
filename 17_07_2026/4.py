from functools import reduce
marks = [10, 20, 30, 40]

for mark in marks:
    total = lambda mark: sum(marks)
    print(total(marks))
    break

def add(num1, num2):
    return num1 + num2

result = reduce(add, marks)
print(result)