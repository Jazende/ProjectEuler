from datetime import datetime

start = datetime.now()

def check_if_prime(nr):
    if nr >= 2:
        for i in range(2, int(nr**(1/2))+1):
            if nr % i == 0:
                return False
    else:
        return False
    return True

y_primes = 0
n_primes = 1

number = 1
incr = 2
add = 2

while True:
    for _ in range(4):
        number += add
        if check_if_prime(number):
            y_primes += 1
        else:
            n_primes += 1

    if y_primes / (y_primes+n_primes) < 0.1:
        break

    add += incr

        
print(f'Runtime: {datetime.now()-start}')
print(f"Proportion: {y_primes}/{n_primes+y_primes} = {y_primes/(n_primes+y_primes)}")
print(f'Sidelength: {add+1}')
