def problem_7(number=10001):
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.
    What is the 10 001st prime number?
    """

    from itertools import count
    primes = [2]
    for x in count(3, step=2):
        counter = 0
        for y in primes:
            if x%y == 0:
                counter+=1
        if counter == 0:
            if len(primes) % 1000 == 0:
                print(len(primes))
            primes.append(x)
        if len(primes) == number:
            print(primes[:20])
            print(primes[len(primes)-1:])
            break

problem_7()
