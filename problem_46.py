import cProfile

##It was proposed by Christian Goldbach that every odd composite number
##can be written as the sum of a prime and twice a square.
##
##9 = 7 + 2×12
##15 = 7 + 2×22
##21 = 3 + 2×32
##25 = 7 + 2×32
##27 = 19 + 2×22
##33 = 31 + 2×12
##
##It turns out that the conjecture was false.
##
##What is the smallest odd composite that cannot be written as the
##sum of a prime and twice a square?

def generate_primes():
    primes = set()
    primes.add(2)
    yield 2
    primes.add(3)
    yield 3
    count = 5
    while True:
        is_prime = True
        for number in primes:
            if count % number == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(count)
            yield count
        count += 2

def generate_composites():
    a = 3
    results = set()
    while True:
        for i in range(2, a):
            for j in range(2, i+1):
                if not i*j in results:
                    results.add(i*j)
                    if i*j % 2 == 1:
                        yield i*j
        a += 1

def problem_46():
    primes_gen = generate_primes()
    primes = [next(primes_gen) for x in range(600)]
    comp_gen = generate_composites()
    composites = sorted([next(comp_gen) for x in range(2000)])
    squares = set([x**2 for x in range(500)])

    for composite in composites:
        adheres_to_conjecture = False
        for prime in [x for x in primes if x < composite]:
            if (composite - prime) / 2 in squares:
                adheres_to_conjecture = True
        if not adheres_to_conjecture:
            return composite

        
print(problem_46())
#cProfile.run('problem_46()')
