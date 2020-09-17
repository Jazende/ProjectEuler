from random import choice
import cProfile

def amicable_number(number):
    results = [1]
    for i in range(2, int(number**(0.5))+1):
        if number % i == 0:
            results.append(i)
            results.append(number // i)
    return sum(results)

cProfile.run('nrs_to_check = {x: amicable_number(x) for x in range(2, 1_000_000)}')

for key, value in nrs_to_check.items():
    print(key, value)

    if key > 30:
        break