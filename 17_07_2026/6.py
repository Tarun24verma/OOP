from functools import reduce

"""
--------------------------------------------------
1. Find the Smallest Number
--------------------------------------------------

Given:

numbers = [42, 17, 68, 9, 31, 24]

Use reduce() to find the smallest number.

Expected result:
9

Condition:
Do not use min().
"""

# numbers = [42, 17, 68, 9, 31, 24]
# s=reduce(lambda x,y: x if x<y else y, numbers)
# print(s)

"""
--------------------------------------------------
2. Find the Total Price of a Shopping Cart
--------------------------------------------------

Each tuple contains:

(product name, price, quantity)

cart = [
    ("Notebook", 50, 3),
    ("Pen", 10, 5),
    ("Bag", 700, 1),
    ("Bottle", 120, 2)
]

Use reduce() to calculate the total cost of the cart.

For each item:

item cost = price * quantity

Expected result:
1140
"""
# # def cost(acc,a):
# #     return acc+a[1]*a[2]

# cart = [
#     ("Notebook", 50, 3),
#     ("Pen", 10, 5),
#     ("Bag", 700, 1),
#     ("Bottle", 120, 2)
# ]
# s=reduce(lambda acc,a:acc+a[1]*a[2],cart,0)
# print(s)

"""
--------------------------------------------------
3. Find the Longest Word
--------------------------------------------------

Given:

words = ["map", "functional", "python", "reduce", "programming"]

Use reduce() to find the longest word.

Expected result:
"programming"

Condition:
Do not use max().
"""

# words = ["map", "functional", "python", "reduce", "programming"]
# s=reduce(lambda c,a: c if len(c)>=len(a) else a, words)
# print(s)

"""
--------------------------------------------------
4. Count the Total Number of Characters
--------------------------------------------------

Given:

words = ["Python", "is", "fun", "to", "learn"]

Use reduce() to find the total number of characters in all the words.

Do not count spaces.

Expected result:
18
"""
# words = ["Python", "is", "fun", "to", "learn"]
# s=reduce(lambda pre,word:pre+len(word),words,0)
# print(s)

"""
--------------------------------------------------
5. Create a Frequency Dictionary
--------------------------------------------------

Given:

letters = ["a", "b", "a", "c", "b", "a", "d", "c"]

Use reduce() to create a dictionary that counts how many times each letter appears.

Expected result:

{
    "a": 3,
    "b": 2,
    "c": 2,
    "d": 1
}

Note:
This problem is slightly more challenging because the accumulated result is a dictionary rather than a number.
"""
letters = ["a", "b", "a", "c", "b", "a", "d", "c"]
def count(check,letter):
    if letter in check:
            check[letter]+=1
    else:
        check[letter]=1
    return check
s=reduce(count,letters,dict())
print(s)