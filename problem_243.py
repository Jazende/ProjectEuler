from fractions import Fraction
import math

##def resilience_factor(denominator):
##    current_amount = 0
##    for x in range(1, denominator):
##        val = Fraction(x, denominator)
##        if val.denominator == denominator:
##            current_amount += 1
##    return current_amount / (denominator-1)
##
##def problem_243(target_fraction):
##    denominator = 2
##    while True:
##        if resilience_factor(denominator) < target_fraction:
##            break
##        denominator += 1
##    return denominator


primes = sieve_as(1000000)

def sieve_as(val):
    primes = [2, 3]
    candidate = 5
    while True:
        if candidate >= val:
            break
        is_prime = True
        sqrt = math.ceil(math.sqrt(candidate+1))
        for prime in primes:
            if candidate % prime == 0:
                is_prime = False
                break
            if prime > sqrt:
                break
        if is_prime:
            primes.append(candidate)
        candidate += 2
    return primes

def problem_243(target_fraction):
    primes.pop(0)
    denominator = 2
    while True:
        if resilience_factor(denominator) < target_fraction:
            break
        new_mul = primes.pop(0)
        print(new_mul)
        denominator *= new_mul
    return denominator

def prime_factors(number):
    factors = set()
    for prime in primes:
        while number % prime == 0:
            number = number // prime
            factors.add(prime)
        if number == 1:
            break
    return factors

print(problem_243(15499/94744))
