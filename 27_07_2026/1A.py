"""Practical 1A — Default and Keyword-Only Arguments
Write a function named `calculate_bill()` that:
Accepts `amount` as a normal argument
Accepts `tax_rate` with a default value of `5`
Accepts `discount` as a keyword-only argument with a default value of `0`
Calculates the final bill after adding tax and subtracting discount
Returns the final amount
Call the function once using default values, and once overriding both `tax_rate` and `discount`.
Expected Sample Output:
```
calculate_bill(1000)                     -> 1050.0
calculate_bill(2000, 10, discount=100)    -> 2100.0
```"""


def calculate_bill(amount, tax_rate=5, *, discount=0)->int:
    return int(amount+((amount*tax_rate)/100)-discount)
# print(calculate_bil(1000))
# print(calculate_bil(2000,10,discount=100))
# #print(calculate_bil(2000,10,100))
# """File "d:\Programming\OOP\27_07_2026\1.py", line 5, in <module>
#     print(calculate_bil(2000,10,100))
#           ~~~~~~~~~~~~~^^^^^^^^^^^^^
# TypeError: calculate_bil() takes from 1 to 2 positional arguments but 3 were given"""
# calculate_bill=lambda amount, tax_rate=5,*, discount=0:amount+((amount*tax_rate)/100)-discount
print(calculate_bill(1000))
print(calculate_bill(2000,10,discount=100))
# print(calculate_bill(2000,10,100))