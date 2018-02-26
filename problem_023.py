def is_perfect_number(number):
    if number % 1000 == 0:
        print(number)
    som = sum(get_proper_divisors(number))
    if som < number:
        return -1
    elif som == number:
        return 0
    else:
        return 1

def get_proper_divisors(number):
    results = [1]
    for n in range(2, int((number+2)/2)):
        if number%n == 0:
            results.append(n)
    return results

def get_abundant_numbers():
    return [x for x in range(12, 28124) if is_perfect_number(x) == 1]

def summation_tactic():
    an_list = get_abundant_numbers()
    sums = []
    for x in an_list:
        for y in an_list:
            if x+y < 28124:
                sums.append(x+y)
    sums = [x for x in list(set(sums)) if x < 28124]
    return sums

def compare():
    list_ = summation_tactic()
    range_ = [x for x in range(24, 28124)]
    reduced = []
    for each in range_:
        if not each in list_:
            reduced.append(each)
    result = sum(reduced) + sum(range(0,24))
    print(result)
    
import cProfile
cProfile.run("compare()")
