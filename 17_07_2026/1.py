"""1. Write a lambda function that returns the square of a number."""
# a=4
# b=lambda a:a*a
# print(b(a))

"""2. Write a lambda function that adds two numbers."""
a,b=5,6
# c=lambda a,b:a+b
# print(c(a,b))

"""3. Write a lambda function that checks whether a number is even."""
# c=lambda a:a%2==0
# print(c(a))

"""4. Convert this normal function into a lambda function:

def greet(name):
    return "Hello " + name"""

name="Tarun"
# c=lambda a:"Hello "+a
# print(c(name))

"""5. Sort the following list of tuples by the second element using a lambda function:

students = [
    ("Ravi", 75),
    ("Anu", 92),
    ("Kiran", 68)
]"""
students = [
    ("Ravi", 75),
    ("Anu", 92),
    ("Kiran", 68)
]
students.sort(key=lambda x : x[1])
print(students)