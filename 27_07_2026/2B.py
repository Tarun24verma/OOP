"""Practical 2B — Lambda with `filter()` and `reduce()`
Given the list:
```
[12, 7, 18, 5, 20, 9, 14]
```
Perform the following:
Use `filter()` with a lambda expression to select only even numbers.
Use `filter()` to select numbers greater than 10.
Use `reduce()` to calculate the sum of all numbers.
Use `reduce()` to calculate the product of all numbers.
Import `reduce` from `functools`. Do not use list comprehensions. Print all results clearly.
Expected Sample Output:
```
Even Numbers: [12, 18, 20, 14]
Numbers > 10: [12, 18, 20, 14]
Sum of Numbers: 85
Product of Numbers: 19051200
```"""


from functools import reduce
nums=[12,7,18,5,20,9,14]
even_number=list(filter(lambda x: x%2==0, nums))
greater=list(filter(lambda x: x>10, nums))
sums=reduce(lambda a,x:x+a, nums)
prod=reduce(lambda a,x:x*a, nums)
print(f"Even Numbers: {even_number}\nNumbers>0: {greater}\nSum of Numbers: {sums}\nProduct of Numbers: {prod}")