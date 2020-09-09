import cProfile
from math import log10, ceil, sqrt

x = 20
y = 10
amount = 1000_0000

def many(amount):
    def fn_wrapper(fn):
        def wrapped(*args):
            print(f'{fn.__name__}: {amount} times')
            print(fn(*args))
            for _ in range(amount):
                fn(*args)
        return wrapped
    return fn_wrapperff

@many(amount)
def mod(x, y):
    return (x % y == 0)

@many(amount)
def comp(x, y):
    return (x / y).is_integer()

print(x % y, x / y, x // y)
cProfile.run('mod(x, y)')
cProfile.run('comp(x, y)')




# primes = [2, 3]
# factorized = {}

# def prime_factors(getal):
#     base = getal
#     prime_facs = []

#     for cur_prime in primes:
#         if getal == 1:
#             break

#         while getal % cur_prime == 0:
#             getal //= cur_prime
#             prime_facs.append(cur_prime)

#             if getal in factorized:
#                 prime_facs += factorized[getal]
#                 getal = 1
#                 break

#     if base == getal:
#         primes.append(base)
#         return [base]

#     factorized[base] = prime_facs

# def problem_070():
#     for i in range(4, 1_00_001):
#         prime_factors(i)

# # problem_070
# cProfile.run('problem_070()')
