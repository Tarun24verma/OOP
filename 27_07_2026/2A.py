"""Practical 2A — Lambda Expression with `map()`
Given a list of numbers:
```
[2, 4, 6, 8, 10]
```
Use a lambda expression with `map()` to:
Create a new list containing the square of every number.
Create another new list with each number increased by `5`.
Do not use list comprehensions. Print both resulting lists.
Expected Sample Output:
```
Squares: [4, 16, 36, 64, 100]
Increased: [7, 9, 11, 13, 15]
```"""


nums=[2,4,6,8,10]
squares=list(map(lambda x:x*x, nums))
increament=list(map(lambda x: x+5, nums))
print(f"Squares: {squares} \nIncreased: {increament}")