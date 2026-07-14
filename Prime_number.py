# def prime(i):
#     if i==2:
#         return True
#     elif i<=1:
#         return False
#     for k in range(2,i):
#         if i%k==0:
#             return False
#     return True

# print(prime(7))

# from sympy import isprime
# print(isprime(13))

from primePy import primes
print(primes.check(13))