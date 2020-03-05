def problem_47():
    from itertools import count
    from math import sqrt

    primes = [2, 3]
    def find_primes(limit):
        curr = 4
        while curr < limit:
            test = 0
            for prime in primes:
                if curr % prime == 0:
                    test += 1
            if test == 0:
                primes.append(curr)
            curr += 1
    find_primes(1000)

    def diff_distinct_factors(getal):
        factors = 0
        if primes[len(primes)-1] < getal:
            extend_primes(1000)
        for prime in primes:
            if getal%prime == 0:
                factors += 1
        return factors

    def extend_primes(limit):
        curr = primes[len(primes)-1]
        new_limit = curr + limit
        while curr < limit:
            test = 0
            for prime in primes:
                if curr % prime == 0:
                    test += 1
            if test == 0:
                primes.append(curr)
            curr += 1

    last_results = []
    for x in count(1):
        i = diff_distinct_factors(x)
        if i >= 4:
            last_results.append(x)
            if x-1 in last_results:
                if x-2 in last_results:
                    if x-3 in last_results:
                        print(x-3)
                        break
            if len(last_results) > 4:
                last_results = last_results[1:]
                    
import cProfile
cProfile.run("problem_47()")
