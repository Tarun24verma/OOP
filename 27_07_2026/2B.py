from functools import reduce
nums=[12,7,18,5,20,9,14]
even_number=list(filter(lambda x: x%2==0, nums))
greater=list(filter(lambda x: x>10, nums))
sums=reduce(lambda a,x:x+a, nums)
prod=reduce(lambda a,x:x*a, nums)
print(f"Even Numbers: {even_number}\nNumbers>0: {greater}\nSum of Numbers: {sums}\nProduct of Numbers: {prod}")