from functools import reduce
def add(first,second):
    return first+second
numbers=[1,2,3,4]
result=reduce(add,numbers)
print(result)