## The first known prime found to exceed one million digits was discovered
## in 1999, and is a Mersenne prime of the form 26972593−1;
## it contains exactly 2,098,960 digits. Subsequently other Mersenne primes,
## of the form 2p−1, have been found which contain more digits.
## However, in 2004 there was found a massive non-Mersenne prime which
## contains 2,357,207 digits: 28433×2^7830457+1.
## Find the last ten digits of this prime number.
import cProfile

def get_power_of_2(power, mod=100):
    base = 1
    for x in range(power):
        base = (base*2)
        if x%200 == 0:
            base = base%(10**mod)
    return base

def problem_97():
    power = get_power_of_2(7830457, 10)
    result = 28433*power+1
    return str(result)[-10:]

def problem_97_power():
    return str(pow(2, 7830457, 10**10)*28433+1)[-10:]


cProfile.run('problem_97()')
cProfile.run('problem_97_power()')
