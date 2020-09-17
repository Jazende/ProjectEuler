import numpy as np
def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)//3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

primes = primesfrom2to(1_000_000)

primes_dict = {x: [] for x in range(1, 7)}


limiter = 10
counter = 1
for prime in primes:
    if prime >= limiter:
        limiter *= 10
        counter += 1
    primes_dict[counter].append(prime)

print([len(primes_dict[x]) for x in range(1, 7)])

print(primes_dict[3])