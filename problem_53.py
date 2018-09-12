import cProfile
from functools import reduce

##There are exactly ten ways of selecting three from five, 12345:
##
##123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
##
##In combinatorics, we use the notation, 5C3 = 10.
##
##In general, nCr = n! / r!(n−r)!   ,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
##It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
##
##How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100,
## are greater than one-million?


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

def combinations(number, subselection):
    return int(factorial(number) / (factorial(subselection) * factorial(number-subselection)))

def problem_53_short(max_=100):
    count = 0
    for i in range(1, max_+1):
        for j in range(1, i+1):
            if combinations(i, j) > 1000000:
                count += 1
    return count

def problem_53_long(max_=100):
    def combo(fact_num, fact_sub, fact_num_sub):
        return int(fact_num / (fact_sub * fact_num_sub))
    
    facts = [0 for _ in range(0, max_+1)]
    facts[0] = 1
    
    for i in range(1, max_+1):
        facts[i] = facts[i-1]*i
    
    count = 0
    for num in range(1, max_+1):
        for sub in range(1, i+1):
            if combo(facts[num], facts[sub], facts[num-sub]) > 1000000:
                #print(num, sub, combo(facts[num], facts[sub], facts[num-sub]))
                count += 1
    return count

def problem_53_combo(max_=100):
    count = 0
    for num in range(1, max_+1):
        fact = 1
        for sub in range(1, num+1):
            fact = fact / sub
            fact = fact * (num-sub+1)
            if fact > 1000000:
                count += 1
    return count

# cProfile.run('problem_53_long(300)')
cProfile.run('problem_53_combo(2500)')

print(problem_53_combo(100))
