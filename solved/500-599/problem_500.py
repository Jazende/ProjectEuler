import cProfile
import numpy as np
from functools import lru_cache

def primes_from_2_to(n):
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)//3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

primes = primes_from_2_to(8_000_000)

''' any number x = (prime_a ** exp_a) * (prime_b ** exp_b) * ...
  divisors for x = (exp_a + 1) * (exp_b + 1) * ... (if exp = 0 -> *1 -> doesn't impact, if exp = 1, -> *2, any prev divisors possible mulled with prime)
                                                   (ex divs(3) = 1, 3. add exp 2, divs(6) = 1, 2, 3, 6 which is either divs mulled by 2)

to find a nr with total of 2**500500 divs, we need exp_a+1 * exp_b+1 * ... to equal 2**500500
since this is a power of two, every factor of this nr is 2, therefor every exp needs to be of the form 2**k - 1 (1, 3, 7, 15, 31, ...)

to start the solution is turned around. starting from the nr of divisors, which is the most optimal nr
ie: 2 divisors  => 2**1 = 2 => 1, 2
 4 divs => 2**1 * 3**1 = 2 * 3 = 6 => 1, 2, 3, 6
 8 divs => 2**3 * 3**1 = 8 * 3 = 24 => 1 2 4 8 3 6 12 24 (2**i * 3**j for i in range(4) for j in range(2))
16 divs => 2**3 * 3**1 * 5**1 = 8 * 3 * 5 = 120

At each step look at the exponents present and bump the lowest of each amount up by val*2+1 up to next power of 2**k - 1
ex going 8 divs:
2**3 * 3**1 * 5**0
as exp we have 3 and 1. If there was more than 1, the lowest is picked. Ie at 2**3 * 3**1 * 5**1, the 3 would be picked for exp-val 1
option a: bump up 3: 2**7 * 3**1 * 5**0 = 128 *  3 * 1 = 384
option b: bump up 1: 2**3 * 3**3 * 5**0 =   8 * 27 * 1 = 216
option c: bump up 0: 2**3 * 3**1 * 5**1 =   8 *  3 * 5 = 120

In the end, we only calculate the difference in increase. For above example:
option a: bump up 3: 2**7 / 2**3 = 2**4 = 16
option b: bump up 1: 3**3 / 3**1 = 3**2 =  9
option c: bump up 0: 5**1 / 5**0 = 5**1 =  5

In the actual solution we save how many primes are at each exp
for example at 8 divs we have 2**3 * 3**1 -> {0: 1, 1: 1, 3:1}, the next step at 16 would be -> {0: 1, 1: 2, 3: 1}
(arbitrarily large nr for 0s counted)
'''

def cleaner_version(primes):
    current_value = 1
    prime_exponents = {0: 0}

    for _ in range(500500):
        next_value = min(prime_exponents.keys(), key=lambda k: primes[sum(value for key, value in prime_exponents.items() if key > k)] ** (k + 1))
        prime_exponents[next_value] = max(0, prime_exponents[next_value] - 1)
        prime_exponents[(next_value*2)+1] = prime_exponents.get((next_value*2)+1, 0) + 1
        current_value *= primes[sum(value for key, value in prime_exponents.items() if key > next_value)-1] ** (next_value + 1)
        current_value %= 500500507

    return current_value

def slightly_more_efficient(primes):
    current_value = 1
    prime_exponents = {0: len(primes)}

    for _ in range(500500):
        min_value = None
        min_calced = None
        for exp_key in prime_exponents.keys():
            to_add = primes[sum(value for key, value in prime_exponents.items() if key > exp_key)] ** (exp_key+1)
            if min_value is None:
                min_calced = to_add
                min_value = exp_key            
            elif to_add < min_calced:
                min_calced = to_add
                min_value = exp_key

        min_value_next_up = (min_value * 2 + 1)
        prime_exponents[min_value] -= 1
        prime_exponents[min_value_next_up] = prime_exponents.get(min_value_next_up, 0) + 1
        current_value *= min_calced
        current_value %= 500500507

    print(current_value)
    return current_value

# cProfile.run('cleaner_version(primes)')
cProfile.run('slightly_more_efficient(primes)')