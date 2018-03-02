from itertools import count
from itertools import permutations as perms
import math

primes = [2]
results = []

def length(input_):
    if type(input_) == str:
        return len(input_)
    if type(input_) == int:
        return len(str(input_))
    else:
        print(type(input_))

def list_primes(number=1000000):
    for x in count(3, step=2):
        if "0" in str(x):
            pass
        elif factors(x):
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

def check_numbers():
    global results
    for prime in primes:
        rots = rotations(prime)
        test = 0
        for rot in rots:
            if not rot in primes:
                test += 1
        if test == 0:
            results += rots
            for rot in rots:
                try:
                    primes.remove(rot)
                except ValueError as v:
                    print(rot, "reeds verwijderd.")

def main():
    list_primes()
    check_numbers()
    print(len(list(set(results))))
if __name__ == '__main__':
    import cProfile
    cProfile.run("main()")
