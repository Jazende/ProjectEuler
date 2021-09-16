from itertools import combinations
from functools import reduce
import decimal

# number - 1 - ->
# for elke combinatie van prime factors:
# -1 ** (lengte primes) [voor elk niveau -1 of 1] * (number-1//product_van_primes)
# bv:
# 30, PF = [2, 3, 5]
# primes: 2     -> 29// 2 -> 14 *  1
# primes:   3   -> 29// 3 ->  9 *  1
# primes:     5 -> 29// 5 ->  5 *  1
# primes: 2 3   -> 29// 6 ->  4 * -1
# primes: 2   5 -> 29//10 ->  2 * -1
# primes:   3 5 -> 29//15 ->  1 * -1
# primes: 2 3 5 -> 29//30 ->  0 *  1

def populate_primes(target=1_000):
    for candidate in range(5, target, 2):
        for prime in primes:
            if candidate % prime == 0:
                break
        else:
            primes.append(candidate)

primes = [2, 3]
populate_primes(1_000_0)

def factor_product(prime_factors):
    return reduce(lambda x, y: x*y, prime_factors)

def get_prime_factors(number):
    prime_factors = []
    for prime in primes:
        if number % prime == 0:
            prime_factors.append(prime)
            while True:
                if number % prime == 0:
                    number //= prime
                else:
                    break
    return prime_factors

def get_full_prime_factors(number):
    prime_factors = []
    for prime in primes:
        while True:
            if number % prime == 0:
                prime_factors.append(prime)
                number //= prime
            else:
                break
    return prime_factors

def all_prime_factor_combinations(prime_factors):
    for idx in range(1, len(prime_factors)+1):
        for combo in combinations(prime_factors, idx):
            yield combo
    return

def resilience_factor(number):
    prime_factors = get_prime_factors(number)
    iter = all_prime_factor_combinations(prime_factors)
    total = number - 1
    while True:
        try:
            combo = next(iter)
        except StopIteration:
            break
        total += ((number-1) // factor_product(combo)) * pow(-1, len(combo))
    resil_factor = decimal.Decimal(total / (number - 1))
    return resil_factor
    
def efficient_find_resilience_factor(target=None):
    if target is None:
        target = decimal.Decimal(4/10)
    prime_index = 0
    value = 1
    while True:
        value *= primes[prime_index]
        if resilience_factor(value) < target:
            print(primes[:9])
            break
        prime_index += 1
    print(value, resilience_factor(value), "<", target)

current_primes = [2, 3]
while True:
    current_nr = factor_product(current_primes)
    target_rf = resilience_factor(current_nr)
    max_current_prime_index = primes.index(max(current_primes))

    current_prime_index = 0
    last_rf_calculated = 1
    while True:
        test_rf = resilience_factor(current_nr*primes[current_prime_index])
        if test_rf > last_rf_calculated:
            current_primes.append(primes[current_prime_index-1])
            break
        else:
            last_rf_calculated = test_rf
        current_prime_index += 1
    
    if last_rf_calculated < decimal.Decimal(15499/94744):
        break

upper_bound = factor_product(current_primes)
current_minimum = resilience_factor(upper_bound)

print(current_primes, factor_product(current_primes))


# target = decimal.Decimal(15499 / 94744)
# check = lambda *x: print(x, factor_product(x), resilience_factor(factor_product(x)), resilience_factor(factor_product(x)) < target)

# check(2, 2, 2, 3, 5, 7, 11, 13, 17, 19, 23) #  892371480

