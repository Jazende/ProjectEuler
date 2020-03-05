import cProfile
import timeit
import math
import time

##The prime 41, can be written as the sum of six consecutive primes:
##41 = 2 + 3 + 5 + 7 + 11 + 13
##This is the longest sum of consecutive primes that adds to a prime below
##one-hundred. The longest sum of consecutive primes below one-thousand
##that adds to a prime, contains 21 terms, and is equal to 953.
##Which prime, below one-million, can be written as the sum of the most
##consecutive primes?

def sieve_as(val):
    primes = [2, 3]
    candidate = 5
    while True:
        if candidate >= val:
            break
        is_prime = True
        sqrt = math.ceil(math.sqrt(candidate+1))
        for prime in primes:
            if candidate % prime == 0:
                is_prime = False
                break
            if prime > sqrt:
                break
        if is_prime:
            primes.append(candidate)
        candidate += 2
    return primes

def prob_50(val):
    # print("Getting primes...", end=" ")
    primes_set = sieve_as(val)
    base_primes_list = sorted(list(primes_set))
    max_prime = max(primes_set)
    # print(f"Got primes. Len: {len(primes_set)}. Max: {max_prime}")

    # Reducing range
    # print("Reducing range...", end=" ")
    reduc = len(primes_set)
    for i in range(len(base_primes_list)):
        sum_ = sum(base_primes_list[i:i+3])
        if sum_ > max_prime:
            reduc = i
            break
    
        
    primes_list = base_primes_list[:reduc+3]
    
    # print(f"Reduced. Len: {len(primes_list)}. Max: {max(primes_list)}")
    
    best_len = 0
    best_result = 0

    # Checken best result vanaf 2:
    value = 0
    count = 0
    for prime in primes_list:
        value += prime
        count += 1
        if value in primes_set:
            best_len = count
            best_result = value
        if value > val:
            break

    # print(f"Beste len vanaf 2: {best_len} met value {best_result}")
    # print(f"Possible better results: ")

    stop = False
    check_len = best_len
    while True:
        for i in range(len(primes_list)-check_len):
            sum_ = sum(primes_list[i:i+check_len])
            if sum_ in base_primes_list:
                if check_len > best_len:
                    best_len =  check_len
                    # print(best_len, sum_)
            if i == 0 and sum_ > val:
                stop = True
            if sum_ > val:
                break
        
        check_len += 1
        if stop:
            break
        if check_len == len(primes_list):
            break
    return best_len
    
# print(prob_50(1000000))
cProfile.run('prob_50(1000000)')
