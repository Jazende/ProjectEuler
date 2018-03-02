from itertools import count
from itertools import permutations as perms
import math

def length(input_):
    if type(input_) == str:
        return len(input_)
    if type(input_) == int:
        return len(str(input_))
    else:
        print(type(input_))

def prime_avertion(input_):
    if "0" in str(input_):
        return False
    elif "2" in str(input_):
        return False
    elif "4" in str(input_):
        return False
    elif "5" in str(input_):
        return False
    elif "6" in str(input_):
        return False
    elif "8" in str(input_):
        return False
    else:
        return True

def prune_primes():
    for prime in primes[4:]:
        if not prime_avertion(prime):
            primes.remove(prime)

def list_primes(number=1000000):
    for x in count(3, step=2):
        if factors(x):
            primes.append(x)
        if x > number:
            break

def factors(poss_prime):
    for y in primes:
        if poss_prime%y == 0:
            return False
        if y > math.sqrt(poss_prime):
            break
    return True

def rotations(waarde):
    return [int(str(waarde)[i:length(waarde)]+str(waarde)[0:i]) for i in range(0, length(waarde))]

def make_number(values):
    return sum([x * 10 ** (len(values)-1-values.index(x)) for x in values])

def spread_numers(d2, d3, d4, d5, d6):
    single_digits = []
    for prime in primes:
        if prime < 10:
            single_digits.append(prime)
        elif 10 <= prime < 100:
            d2.append(prime)
        elif 100 <= prime < 1000:
            d3.append(prime)
        elif 1000 <= prime < 10000:
            d4.append(prime)
        elif 10000 <= prime < 100000:
            d5.append(prime)
        elif 100000 <= prime < 1000000:
            d6.append(prime)
    return single_digits

def check_numbers(group):
    results = []
    for prime in group:
        rots = rotations(prime)
        test = 0
        for rot in rots:
            if not rot in group:
                test += 1
        if test == 0:
            results += rots
    return results

def main(results, d2, d3, d4, d5, d6):
    print("listing primes")
    list_primes()
    print("pruning")
    prune_primes()
    print("spreading numbers")
    results += spread_numers(d2, d3, d4, d5, d6)
    for group in [d2, d3, d4, d5, d6]:
        results += check_numbers(group)
        print("checking group ", length(group[0]), len(results))
    return results

    
if __name__ == '__main__':
    primes = [2]
    results = []
    d2 = []
    d3 = []
    d4 = []
    d5 = []
    d6 = []
    import cProfile
    cProfile.run("main(results, d2, d3, d4, d5, d6)")
