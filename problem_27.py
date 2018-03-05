from math import sqrt
import cProfile

def main():
    primes = [2]
    combos = {}
    sqrts = {}

    def list_sqrt(number):
        upper_bound = number
        for i in range(upper_bound):
            sqrts[i] = sqrt(i)
            
    def list_primes(number=1000000):
        list_sqrt(number)
        for x in range(3, number+1, 2):
            if factors(x):
                primes.append(x)
            if x > number:
                break

    def factors(poss_prime):
        for y in primes:
            if poss_prime%y == 0:
                return False
            if y > sqrts[poss_prime]:
                break
        return True

    def make_combos():
        for b in primes1000:
            for a in [x-b-1 for x in primes1000 if -1000 <= (x-b-1) <= 1000]:
                combos[(a, b)] = 0

    def cleanse_by_n(n_value, combinaties):
        results = {}
        print("Cleansing value", n_value, len(combinaties))
        for combo in combinaties.keys():
            if n_value*(n_value+combo[0]) + combo[1] in primes:
                results[combo] = combinaties[combo] + 1
        return results
                
    print("Making primes")
    list_primes()
    primes1000 = [x for x in primes if x < 1001]
    print("Making combos")
    make_combos()
    n = 2
    while len(combos) > 1:
        combos = cleanse_by_n(n, combos)
        n += 1
        if len(combos) < 2:
            for combo in combos.keys():
                print(combo, end = ' ')
                print(combo[0] * combo[1])

cProfile.run("main()")
