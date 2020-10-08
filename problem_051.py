# import numpy as np
# from math import log10, floor, ceil

# def primesfrom2to(n):
#     # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
#     """ Input n>=6, Returns a array of primes, 2 <= p < n """
#     sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
#     sieve[0] = False
#     for i in range(int(n**0.5)//3+1):
#         if sieve[i]:
#             k=3*i+1|1
#             sieve[      ((k*k)//3)      ::2*k] = False
#             sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
#     return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

# min_prime = 56_000
# max_prime = 10_000_000

# min_int = floor(log10(min_prime))
# max_int = ceil(log10(max_prime)) + 1

# primes = primesfrom2to(max_prime)
# primes_digit_eq = {x: {(i, j): set() for i in range(x) for j in [y for y in range(x) if not y == i]} for x in range(min_int, max_int)}

# count = 0
# for prime in primes:
#     if prime < 10_000:
#         continue
#     if prime > max_prime:
#         break
#     prime_str = str(prime)
#     len_prime = len(prime_str)
#     for x in range(len_prime):
#         for y in [i for i in range(len_prime) if not i == x]:
#             count += 1
#             if prime_str[x] == prime_str[y] and x < y:
#                 # print(prime, len_prime, x, y)
#                 primes_digit_eq[len_prime][(x, y)].add(prime)

# # for l in range(5, max_int):
# #     for x in range(l):
# #         for y in [j for j in range(l) if not j == x]:
# #             print(l, x, y, len(primes_digit_eq[l][(x, y)]))
# #     break

# print(primes_digit_eq[5][(0, 1)])