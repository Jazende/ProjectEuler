import math
import cProfile
from itertools import permutations

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9][::-1]
sieve = set()
sieve.add(2)
sieve.add(3)

def run_sieve(max_nr=987654321):
    ceil = math.ceil(math.sqrt(max_nr+1)+1)+100
    for i in range(5, ceil, 2):
        add = True
        for test in sieve:
            if i % test == 0:
                add = False
        if add:
            sieve.add(i)

def is_prime(prime_test):
    l = len(prime_test)
    nr = sum([prime_test[i-1]*(10**(l-i)) for i in range(1, l+1)])
    for test in sieve:
        if nr % test == 0:
            return False
    return True

def euler_41():
    run_sieve()
    count = 0
    for i in range(1, 10)[::-1]:
        perms = permutations([1, 2, 3, 4, 5, 6, 7, 8, 9][:i][::-1], i)
        while True:
            try:
                p = next(perms)
                count += 1
                if is_prime(p):
                    l = len(p)
                    return sum([p[i-1]*(10**(l-i)) for i in range(1, l+1)])
            except StopIteration:
                break
    
print(euler_41())
cProfile.run('euler_41()')
