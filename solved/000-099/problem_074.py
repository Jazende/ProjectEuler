from functools import lru_cache
import time

@lru_cache(maxsize=9)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

@lru_cache(maxsize=None)
def factorial_digit(number):
    digits = []
    while True:
        last_digit = number % 10
        digits.append(last_digit)
        number -= last_digit
        if number == 0:
            break
        number //= 10
    
    return sum([factorial(digit) for digit in digits])

def chain(start):
    nrs = [start]
    while True:
        start = factorial_digit(start)
        if start in nrs:
            # Gets the chain length
            # return len(nrs) - nrs.index(start)

            # Gets first index of repeat
            # return nrs.index(start)

            # Gets full length of non-repeating 
            return len(nrs)
        nrs.append(start)


# for x in [145, 169, 871, 872, 69, 78, 540]:
#     print(f'{x:>5}> {chain(x):>3}')

# print('------------')

count = len([x for x in range(1_000_000) if chain(x) == 60])
print(count)