import math
import cProfile

## top_left diagonal -> even**2 + 1
## bot_left diagonal -> even**2 + (even+1**2 - even**2) //2  +1
## bot_right diagonal -> oneven ** 2
## top_right diagonal -> oneven**2 + (oneven+1**2 - even**2)//2+1

## Voor elke waarde van kant:
        ## 1 waarde: i**2 (als even +1)
        ## 2 waarde: kant

primes = [2, 3]

def get_primes(max_=100000):
    global primes
    for num in range(max(primes), max(primes)+max_, 2):
        poss_prime = True
        sqrt = math.sqrt(num)
        for prime in primes:
            if num%prime == 0:
                poss_prime = False
            if prime > sqrt:
                break
        if poss_prime:
            primes.append(num)
    return primes

def values_voor(i):
    x = i**2
    y = x + i + 1
    if i % 2 == 0:
        x += 1
    return [x, y]


def problem_58():
    global primes
    



    










##

##
##def prob_58():
##    prime_list = get_primes(1000)
##    amount_primes = 0
##    amount_checked = 0
##    value = 1
##    edge = 0
##    while True:
##        edge += 2
##        for i in range(3):
##            value += edge
##            amount_checked += 1
##            while value > prime_list[-1]:
##                prime_list = get_primes(100000, prime_list)
##            if value in prime_list:
##                amount_primes += 10
##        value += edge
##        if amount_checked % 100 == 0:
##            print(edge, value, "\t", amount_primes//10, amount_checked)
##        if amount_primes < amount_checked:
##            break
##    print(edge)
##    
##
##
##def prob_58():
##    prime_list = get_primes(1000)
##    primes = 0
##    numbers = 0
##    spiral = spiral_numbers()
##    next(spiral)
##    while True:
##        for i in range(4):
##            numbers += 1
##            corner = next(spiral)
##            while corner > max(prime_list):
##                prime_list = get_primes(1000, prime_list)
##            if corner in prime_list:
##                primes += 1
##        if numbers % 100 == 0:
##            print(numbers, len(primes), primes/numbers)
##        if (primes / numbers) < 0.1 :
##            break
##
##    global edge
##    print(edge, corner)
##    
#####cProfile.run('prob_58()')
####print(prob_58())


##edge = 0
##
##def spiral_numbers():
##    value = 1
##    yield value
##    global edge
##    while True:
##        edge += 2
##        for i in range(4):
##            value += edge
##            yield value
##
##def test_1():
##    gen = spiral_numbers()
##    for i in range(1, 100000):
##        x = next(gen)
