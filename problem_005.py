def problem_5(number=20):
    """
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all
    of the numbers from 1 to 20?
    """
    from collections import Counter
    def factors(getal):
        factors = []
        start = 2
        while True:
            while True:
                if getal % start == 0:
                    factors.append(start)
                    getal = int(getal/start)
                else:
                    break
            if getal == 1:
                break
            else:
                if start == 2:
                    start += 1
                else:
                    start += 2
        return factors

    factors_dict = {}
    for x in range(1, number+1):
        for key in Counter(factors(x)).keys():
            if key in factors_dict:
                factors_dict[key] = max(Counter(factors(x))[key], factors_dict[key])
            else:
                factors_dict[key] = Counter(factors(x))[key]
    print(factors_dict)
    result = 1
    for key in factors_dict.keys():
        result = result * (key ** factors_dict[key])
    print(result)

problem_5()