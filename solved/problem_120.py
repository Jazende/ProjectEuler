import cProfile

min_a = 3
max_a = 1000

def square_reminder(a, n):
    sq = a**2
    sub = a-1
    sup = a+1
    first = 1
    second = 1
    for x in range(n):
        first = (first * sub) % sq
        second = (second * sup) % sq
    return (first + second) % sq

# sum of all [max square remainder for 1 -> 2a+3 (per 2)] for a in min_a -> max_a+1
# print(sum([max([square_reminder(a, n) for n in range(1, (2*a)+3, 2)]) for a in range(min_a, max_a+1)]))


# https://projecteuler.net/thread=120 -> HV

sum_ = 0
for a in range(3, 1001):
    sum_ += a*a - 2*a if a%2==0 else a*a - a
print(sum_)

