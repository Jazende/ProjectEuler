import cProfile
import time

def get_primes():
    primes = [2, 3]
    yield 2
    yield 3
    check = 5
    while True:
        is_prime = True
        for prime in primes:
            if check%prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(check)
            yield check
        check += 2

def prob_69(tar):
    primes = get_primes()
    max_ = 0
    cur_val = next(primes)
    while True:
        max_ = max(cur_val, max_)
        new_val = cur_val * next(primes)
        if new_val > tar:
            return cur_val
        else:
            cur_val = new_val

prob_69(1000000)
#cProfile.run('prob_69(1000000)')
