from fractions import Fraction
import cProfile


def highest_common_factor(number):
    pass

def prob_72(tar):
    factors = {}
    for x in range(1, tar):
        factors[x] = []

#print(prob_72(100))
cProfile.run('prob_72(1000000)')
