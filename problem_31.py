## upper bound 9999999
from functools import reduce
def fact(fact):
    if fact == 0:
        return 1
    elif fact == 1:
        return 1
    elif fact == 2:
        return 2
    return reduce(lambda x, y: x*y, [x for x in range(1, fact+1)])
def sf(number):
    return sum([fact(int(x)) for x in str(number)])
built_nr = lambda a, b, c, d, e, f, g: int("{}{}{}{}{}{}{}".format(str(a), str(b), str(c), str(d),
                                                                   str(e), str(f), str(g)))
sf10 = [fact(x) for x in range(0, 10)]
upper_bound = fact(9)*7

for a in range(10):
    if sf(built_nr(a, 0, 0, 0, 0, 0, 0)) > upper_bound:
        break
    for b in range(10):
        print(built_nr(0, 0, 0, 0, 0, a, b), "out of 100")
        if sf(built_nr(a, b, 0, 0, 0, 0, 0)) > upper_bound:
            break
        for c in range(10):
            if sf(built_nr(a, b, c, 0, 0, 0, 0)) > upper_bound:
                break
            for d in range(10):
                if sf(built_nr(a, b, c, d, 0, 0, 0)) > upper_bound:
                    break
                for e in range(10):
                    if sf(built_nr(a, b, c, d, e, 0, 0)) > upper_bound:
                        break
                    for f in range(10):
                        if sf(built_nr(a, b, c, d, e, f, 0)) > upper_bound:
                            break
                        for g in range(10):
                            if a == b == c == d == e == f == 0:
                                break
                            nr = built_nr(a, b, c, d, e, f, g)
                            if nr == sf(nr):
                                print(nr)
