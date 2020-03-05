def problem_40():
    from itertools import count
    prod = 1
    amount = 0
    for x in count(1):
        for y in str(x):
            amount += 1
            if amount in [1, 10, 100, 1000, 10000, 100000]:
                prod *= int(y)
            if amount in [1000000]:
                prod *= int(y)
                print(prod)
        if amount > 1000000:
            break
problem_40()
