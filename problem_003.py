def problem_3(number=600851475143):
    """Problem 3
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """
    import time
    factors = []
    start = 2
    start_time = time.clock()
    while True:
        while True:
            if number % start == 0:
                factors.append(start)
                number = int(number/start)
            else:
                break
        if number == 1:
            break
        else:
            if start == 2:
                start += 1
            else:
                start += 2

    print(factors[len(factors)-1])
    print(time.clock()-start_time)

problem_3()
