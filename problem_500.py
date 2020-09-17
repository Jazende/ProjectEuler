'''
The number of divisors of 120 is 16.
In fact 120 is the smallest number having 16 divisors.

Find the smallest number with 2500500 divisors.
Give your answer modulo 500500507.
'''

'''
120 (16divs) = 2*2*2*3*5 = 2 ^ 3 * 3 ^ 1 * 5 ^ 1
2 ^ 3 -> 3+1
3 ^ 1 -> 1+1
5 ^ 1 -> 1+1 
(3+1) * (1+1) * (1+1) -> 16

900 (27divs) = 2*2*3*3*5*5 = 2 ^ 2 * 3 ^ 2 * 5 ^ 2
2 ^ 3 -> 2+1
3 ^ 1 -> 2+1
5 ^ 1 -> 2+1 
(2+1) * (2+1) * (2+1) -> 27

'''

primes = [2, 3]
def get_primes(upto=x):
    global primes
    

def count_divs(x):
    count = 0
    for i in range(1, x+1):
        if x%i == 0:
            count += 1
    return count

def calc_divs(x):
