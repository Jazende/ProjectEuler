from itertools import permutations

##The arithmetic sequence, 1487, 4817, 8147,
##in which each of the terms increases by 3330,
##is unusual in two ways:
##    (i) each of the three terms are prime, and,
##    (ii) each of the 4-digit numbers are permutations of one another.
##
##There are no arithmetic sequences made up of three 1-, 2-,
##or 3-digit primes, exhibiting this property,
##but there is one other 4-digit increasing sequence.
##
##What 12-digit number do you form by concatenating the three terms
##in this sequence?

def get_primes(max_=10000):
    primes = [2, 3]
    for num in range(5, max_, 2):
        poss_prime = True
        for prime in primes:
            if num%prime == 0:
                poss_prime = False
        if poss_prime:
            primes.append(num)
    return primes

def problem_49(target=3334):
    primes = get_primes(target*3)
    poss_values = []
    for seq in range(1000, target):
        perms = permutations([int(x) for x in str(seq)])
        prime_perms = set([int("".join([str(i) for i in x])) for x in perms if int("".join([str(i) for i in x])) in primes])
        prime_perms = [x for x in prime_perms if 1000 <= x <= 9999]
        if len(prime_perms) >= 3:
            poss_values.append([seq,prime_perms])
    print(len(poss_values))
    results = []
    for poss in poss_values:
        perms = permutations(poss[1], 3)
        for perm in perms:
            perm = sorted(perm, reverse=True)
            a = perm[0]-perm[1]
            b = perm[1]-perm[2]
            if a == b:
                if not sorted(perm) in results:
                    results.append(sorted(perm))
               # print(poss, perm, a, b)
    return results

print(problem_49(3334))
