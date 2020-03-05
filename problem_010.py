def problem_10(target=2000000):
    """The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million."""
    from math import sqrt
    primes = [2, 3]
    aantal = 0
    for i in range(5, target+1, 2):
        count = 0
        aantal += 1
        for prime in primes:
            if prime > sqrt(i):
                break
            if i%prime == 0:
                count +=1
        if count == 0:
            primes.append(i)
        if aantal % 10000 == 0:
            print("Tested ", aantal)
    print(len(primes))
    print(sum(primes))
    return primes

problem_10()
