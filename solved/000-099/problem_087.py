import math
from itertools import combinations
import cProfile

value = 50000000
max_prime = math.ceil(math.sqrt(value))
primes = [2, 3]
for i in range(5, max_prime, 2):
    prime_candidate = True
    ceil = math.ceil(math.sqrt(i))
    for prime in primes:
        if i % prime == 0:
            prime_candidate = False
            break
        if prime > ceil:
            break
    if prime_candidate:
        primes.append(i)
        
def problem_087():
    squares = [x**2 for x in primes if x**2 <= value]
    cubes = [x**3 for x in primes if x**3 <= value]
    fourth = [x**4 for x in primes if x**4 <= value]
    print(len(squares), len(cubes), len(fourth))
    x = set()
    for fo in fourth:
        for cu in cubes:
            for sq in squares:
                if sq+cu+fo < value:
                    x.add(sq+cu+fo)
    print(len(x))
cProfile.run('problem_087()')
